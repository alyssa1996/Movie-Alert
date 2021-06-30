import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210701"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# imax가 하루에도 시간을 달리하여 여러 영화를 상영한다는 것을 눈으로 확인하고 수정하여 짠 코드
imax_movie_list = []
movie_list = soup.select('div.col-times')

# 모든 영화 리스트에 대하여 imax 상영관 표시가 있는지 확인하고, imax 상영관이 있는 영화들만 imax_movie_list에 삽입
for movie in movie_list:
    movie_title = movie.select_one('div.info-movie > a > strong').text.strip()
    imax = movie.select_one('span.imax')
    if imax:
        imax_movie_list.append(movie_title)

'''
처음에는 imax가 하루 영화리스트 중 3번 등장하는 것을 확인하고 아래 강의 예제 코드를 3번 돌리려고 했으나 그러면
첫번째 영화만 3번 출력되는 것을 확인하고, 저렇게는 각 영화에 imax 상영관이 있는지 확인할 수 없을거라 판단하고 
모든 영화를 확인하는 방향으로 수정. 하루에 상영되는 영화의 갯수가 아무리 많다하더라도 한정적이기 때문에 가능하다고 생각.
'''

# imax가 하루에 한 영화에 대해서만 오픈한다는 가정하에 강의 내에서 짜여진 코드
# imax = soup.select_one('span.imax')
# if imax:
#     imax_movie = imax.find_parent('div', class_='col-times')
#     movie_title = imax_movie.select_one('div.info-movie > a > strong').text.strip()
#     print("imax theater for movie '%s' is opened"%movie_title)
# else:
#     print('imax theater is not opened')