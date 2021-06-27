'''
웹사이트는 HTML이라는 형식으로 쓰여진 문서이다.
우리는 HTML 문서에 담긴 내용을 가져오기 위해서
파이썬 라이브러리인 requests를 사용한다.
그리고 가져온 HTML 문서에서 필요한 부분을 뽑아내는 것이
크롤링의 시작이라고 볼 수 있다.
그렇다면 BeautifulSoup는 왜 사용하는 것일까?
requests로 요청한 HTML을 프린트해보면 매우 길고 뭐가 뭔지
알아보기 어렵다는 느낌을 받을 것이다.
그렇기 때문에 HTML 문서를 탐색해서 원하는 부분만 쉽게
뽑아내야 하고, 이를 위해 BeautifulSoup을 사용하는 것이다.
http://hleecaster.com/python-web-crawling-with-beautifulsoup/
'''

import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210701"
html = requests.get(url)
print(html.text)
