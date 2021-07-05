# Movie-Alert

해당 코드는 [인프런](https://www.inflearn.com/)에 오픈되어 있는 [파이썬으로 영화 예매 오픈 알리미 만들기](https://inf.run/wwX8) 강좌를 수강하며 작성되었습니다.

<br></br>
## Study Log
#### 2021-06-27: 섹션 0.0 준비 <br>
TIL - [BeautifulSoup과 requests](https://velog.io/@jisu0807/TIL-requests%EC%99%80-BeutifulSoup-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%82%AC%EC%9A%A9)
#### 2021-06-29: 섹션 1.1 _ bs4로 상영시간표 영화 제목 크롤링하기 <br>
TIL - [BeautifulSoup에서 select 메소드 사용하기](https://velog.io/@jisu0807/%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-BeautifulSoup%EC%97%90%EC%84%9C-find%EC%99%80-select-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
#### 2021-06-30 : 섹션 1.2 & 1.3 <br>
코드 내의 수정 부분<br>
  > 강의에서는 하루에 IMAX 영화관에서 상영되는 영화가 하나라고 가정하고 코드가 작성됨<BR>
  > 하지만 하루에도 다양한 영화가 IMAX 영화관에서 사용되는 것을 확인함<BR>
  > 이에 따라 하나의 영화만 보여주는 것이 아닌, IMAX에서 상영되는 모든 영화를 보여주는 방식으로 수정함.
  ```PYTHON
  #기존 코드
  imax = soup.select_one('span.imax')
  if imax:
    imax_movie = imax.find_parent('div', class_='col-times')
    movie_title = imax_movie.select_one('div.info-movie > a > strong').text.strip()
    print("imax theater for movie '%s' is opened"%movie_title)
  else:
    print('imax theater is not opened')
  ```
  ```python
  #변경한 코드
  imax_movie_list = []
  movie_list = soup.select('div.col-times')

  # 모든 영화 리스트에 대하여 imax 상영관 표시가 있는지 확인하고, imax 상영관이 있는 영화들만 imax_movie_list에 삽입
  for movie in movie_list:
    movie_title = movie.select_one('div.info-movie > a > strong').text.strip()
    imax = movie.select_one('span.imax')
    if imax:
        imax_movie_list.append(movie_title)
  print(imax_movie_list)
  ```
#### 2021-07-01: 섹션 2.1 & 2.2 _ 텔레그렘봇 만들기 <br>
  코드 수정 부분
  > 1. telegram bot의 토큰과 나의 user id를 다른 파일에 넣어두고 필요로 하는 코드에서 모듈로 불러와 사용하게 함.<br>
  그리고 해당 파일은 .gitignore에 포함시킴. 그리하여 지금 당장 토큰과 아이디가 외부에 드러나지 않도록 조치를 취함.<br>
  > 2. 추가적으로 봇이 보내는 메시지에 날짜와 imax에서 오픈하는 모든 영화를 보여주도록 html url에서 date 부분을 분리하여 새로운 변수에 날짜를 넣고 해당 변수를 url에 연결되도록 함. <br>
  이를 통해 차후 유연한 date값을 이용한 기능 확장이 가능하도록 함.
  ```python
  #2번 코드 변경전
  url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210701"
  #변경후
  date = "20210701"
  url = ""http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date="+date
  ```

  #### 2021-07-02: 섹션3 _ 스케줄러 만들기<br>
  APScheduler 활용
  - 사용 이유 : 파이썬 코드를 주기적으로 수행하기 위해서
  - BlockingScheduler는 단일스케줄러, BackgroundScheduler는 다중스케줄러
  - 공식문서 : https://apscheduler.readthedocs.io/en/stable/userguide.html 
  
  코드 수정 부분
  - 사용자가 입력한 날짜를 받아와서 imax 상영관 오픈 영화를 보여줌
  - telegram 라이브러리를 이용하는 코드를 크롤링하는 코드에서 분리시킴 -> [분리된 코드](telegram_message.py) 
  
  개선해야 할 부분 / 앞으로 해야할 부분
  - 현재 scheduler를 pasuse 시키는 부분이 따로 없음. 
  사용자가 끝내도록 하는 기능을 추가하거나, 아예 사용자에게 처음에 이 봇을 이용하여 사용 가능한 기능을 보여준 후 사용자가 선택하는 기능들만 그때 그때 실행하도록 코드를 수정할 예정
  
  #### 2021-07-05: 섹션4 _ 서버 구축<br>
  서버를 구축하는 이유 
  * aws에 서버를 구축하는 것은 가상의 컴퓨터를 하나 빌려오는 것이라고 볼 수 있다. 그래서 우리가 여태 개발자의 컴퓨터에서 실행시키던 프로그램을 그 가상의 컴퓨터에 올려서 우리가 컴퓨터를 켜고 일일이 실행시키지 않아도 알아서 돌아가도록 하기 위함
  
  어려웠던 점
  * 윈도우 환경에서는 PuTTY라는 프로그램을 사용해서 AWS EC2를 실행시켜야 했는데, 이 과정이 좀 까다로웠다. 다행히 좋은 자료를 발견하여 무사히 잘 돌아가도록 환경을 구축할 수 있었다.
  * Reference - https://mozi.tistory.com/191
  
  시도했으나 다시 보완해야 하는 부분
  * 사용자의 메세지에 따라 scheduler가 메세지 보내는 부분을 컨트롤하도록 코드를 수정하려하였으나 telegram_bot의 getUpdate는 누적 메세지를 모두 가지고 있어서 마지막 메세지가 지금 처음 보내는 건지 저번에 보냈던 것의 마지막인지 구별을 못함. 그래서 stop를 받았을 때 스케줄러가 멈추게 하려던 코드는 불가능. stop를 받고 나서 다시 프로그램을 돌려도 마지막 메세지는 stop이기 때문에 다른 일을 하지 않고 스케줄러가 멈추게 됨. -> 보완 필요

  추가적으로 해야 할 것
  1. 구현하고 싶은 기능 리스트 업
  2. 구현완료 후 다른 사람의 핸드폰에서도 실행되는지 확인
  3. 프로그램을 실행시키는 방법을 ReadME에 동영상과 함께 첨부
