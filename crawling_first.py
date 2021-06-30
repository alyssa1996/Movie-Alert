import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210701"
html = requests.get(url)
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
movie_list = soup.select('div.info-movie')
for i in movie_list:
    print(i.select_one('a > strong').text.strip())
