# Made by smile._.wonnie

import time
import pyautogui as pag
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Chrome Driver를 이용하여 인스타그램 URL에 접속
url = 'https://www.instagram.com'
driver = webdriver.Chrome('chrome driver의 경로 입력')
driver.get(url)
time.sleep(2)

# 아이디와 비밀번호를 입력
username = '아이디 입력'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(username)
password = '비밀번호 입력'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)

# 로그인 하기 
input_pw.submit()
time.sleep(8)

# 정보 다음에 저장하기 버튼
login_later_button = driver.find_elements_by_css_selector('div.cmbtv')[0]
login_later_button.click()
time.sleep(3)

# 알람 끄기 버튼
alam_later_button = driver.find_elements_by_css_selector('div.mt3GC')[0]
alam_later_button.click()
time.sleep(3)

# '선팔하면 맞팔해요'에 대하여 검색
# 이외에도 다양한 검색어로도 가능
driver.get('https://www.instagram.com/explore/tags/%EC%84%A0%ED%8C%94%ED%95%98%EB%A9%B4%EB%A7%9E%ED%8C%94/')
time.sleep(5)

SCROLL_PAUSE_TIME = 2.0
photo_url_list = []

# 몇번 스크롤하여 정보를 가져올지 결정 (아래의 예시는 스크롤 10번)
for i in range(0, 10):
    page_string = driver.page_source
    soup = BeautifulSoup(page_string, 'lxml')

    # 한 개의 class는 3개의 이미지에 대한 정보를 담고 있음
    for link1 in soup.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
        for i in range(0, 3):
            title = link1.select('a')[i]
            real = title.attrs['href']
            photo_url = url + real
            photo_url_list.append(photo_url)

    #스크롤
    last_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue

# 몇 개의 데이터를 수집하였는지 출력
num_data = len(photo_url_list)
print('The number of Links: {0}'.format(num_data))

print(photo_url_list)

count = 1

for photo_url in photo_url_list :

    # scrpy 실행창을 클릭하여 활성화
    pag.click((1194, 400))

    # 홈으로 이동하기
    pag.click((1269, 726))
    time.sleep(1)

    # 홈화면의 크롬을 클릭하여 실행
    pag.click((1194, 663))
    time.sleep(3)
    
    # 주소창을 클릭
    pag.click((1252, 96))
    time.sleep(3)

    # URL 주소를 입력
    pag.typewrite(photo_url)
    time.sleep(1)

    # 해당 URL로 이동
    pag.click((1415, 680))
    time.sleep(6)

    # 좋아요 누르기 (사진을 두번 더블 클릭)
    pag.click((1269, 343))
    pag.click((1269, 343))
    time.sleep(2)

    # 사용자 아이디 클릭
    pag.click((1190, 178))
    time.sleep(5)

    # 팔로우 버튼을 인식
    pag.click((1222, 225))
    time.sleep(2)

    # 홈으로 이동하기
    pag.click((1269, 726))
    time.sleep(3)
    print('The number of people followed : {0}'.format(count))
    count += 1

print('All Finish! (Total count: {0})'.format(count-1))
