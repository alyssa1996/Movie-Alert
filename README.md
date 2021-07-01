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
