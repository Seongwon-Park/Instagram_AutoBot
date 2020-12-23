# Instagram-Bot
Using selenium and pyautogui

## Youtube Link
Video : [[Youtube](https://www.youtube.com/watch?v=ardanu91Y4I&feature=youtu.be)]

# 목표
* 인스타그램 봇을 이용하여 "맞팔", "선팔하면 맞팔해요" 등의 태그를 올린 유저를 팔로우 및 좋아요 함으로써 내 계정의 노출도를 증가하여 보고자 한다.

     (+ 과연 사람들은 몇 퍼센트의 비율로 나에게 맞팔하여 줄까?)

# 알고리즘
1. selenium과 chrome driver를 이용하여 인스타그램을 자동으로 접속 및 로그인한다.
2. 로그인을 마친 상태에서 특정 태그에 대하여 검색하고, 그 결과로 올라온 게시글의 URL을 수집한다. 
3. scrcpy를 이용하여 안드로이드 폰 화면을 미러링 한다. (Mac OS를 사용 중이기 때문이다.)
4. pyautogui를 이용하여 미러링된 android폰을 자동화하여 해당 URL로 이동, 좋아요 및 팔로우를 반복한다.

# 문제점 및 해결
1. selenium으로 검색 후, 좋아요 와 팔로우 를 반복하면 인스타그램으로부터 차단을 당한다.
 - 이는 selenium과 pyautogui로 해결하였다. (안드로이드 폰은 봇 감지로부터 컴퓨터 환경보다 조금이나마 자유로웠다.) 
2. 좋아요를 하기위하여 하트를 클릭하여야 하는데, 이 때 사진의 높이가 다 다르므로, 하트의 위치도 다 달랐다.
 - 이는 사진을 두번 더블 클릭하는 방법으로 해결하였다.
3. 팔로우를 할 때, 사용자의 자기소개의 분량에 따라 팔로우 버튼의 위치가 달랐다.
 - locateCenterOnScreen을 이용하여 팔로우 버튼을 인식하여 클릭하고자 하였으나, 인식의 정확도가 낮았다.
 - 따라서 모바일 어플리케이션이 아닌 크롬으로 들어갈 경우 팔로우 버튼의 위치가 동일하다는 점을 이용하였다.
 
 # 시작 및 결과
 * 2020년 12월 22일 (화) 22:00 ~ 진행중
 
 * 시작시점의 팔로워 / 팔로잉 : (195 / 200)
 * 종료시점의 팔로워 / 팔로잉 : ( 217 / 469 )
 
 * 팔로잉 증가량 : 269 명
 * 총 팔로워 수: 22 명
 
 * 맞팔 비율 :  8 % (247 명은 맞팔을 하지 않았다.)

# 향후 계획
* 너무 단순한 로직이다보니, 인스타그램에 의해 쉽게 제지당했다. 좀 더 복잡한 로직을 이용한 자동화 봇을 만들어보자.

   -> 제지당하지 않는 자동화 봇을 통하여 2000명을 팔로잉 해보자. (예상 팔로워 증가량 : 200여 명)

# 참고 자료
[노마드코더 님의 유튜브] - https://www.youtube.com/watch?v=uUIFN0mHpE4&t=283s

[코딩으로 이것저것 님의 블로그] - https://m.blog.naver.com/jsk6824/221765884364

[잡다한 IT 지식 님의 블로그] - https://m.blog.naver.com/kokoyou7620/222069536659 

[scrcpy 다운로드] - https://github.com/Genymobile/scrcpy
