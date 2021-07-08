import requests
from bs4 import BeautifulSoup
from datetime import datetime
from telegram_message import *

current_date = datetime.now().strftime('%Y%m%d')

def run_crawler(movie_date):
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date="+movie_date
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    movie_list = soup.select('div.col-times')
    return get_imax_movies(movie_list)

#모든 영화 중 imax 상영관이 표시되어 있는 영화만 추출
def get_imax_movies(movie_list):
    movie_titles = []
    for movie in movie_list:
        movie_title = movie.select_one('div.info-movie > a > strong').text.strip()
        if movie.select_one('span.imax'):
            movie_titles.append(movie_title)
    return movie_titles

def check_movie_list(imax_movie_list, movie_date):
    if imax_movie_list:
        if current_date == movie_date:
            current_message = "오늘"
        else:
            current_message = movie_date+"에"
        
        current_message += " IMAX 예매가 열리는 영화는 "+', '.join(imax_movie_list)+"입니다!"
        add_message = '\n 다른 날짜의 IMAX 오픈 영화를 알고 싶다면 YYYYMMDD 형태로 날짜를 입력해주세요!'
        send_bot_message(current_message+add_message)
        return True
    
    return False