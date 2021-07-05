import requests
from bs4 import BeautifulSoup
from datetime import datetime
from telegram_message import *
from apscheduler.schedulers.blocking import BlockingScheduler

last_bot_updates = get_update_counts()

current_date = datetime.now().strftime('%Y%m%d')
movie_date = current_date

#모든 영화 중 imax 상영관이 표시되어 있는 영화만 추출
def get_imax_movies(movie_list):
    movie_titles = []
    for movie in movie_list:
        movie_title = movie.select_one('div.info-movie > a > strong').text.strip()
        if movie.select_one('span.imax'):
            movie_titles.append(movie_title)
    return movie_titles

def job_function():
    # if get_last_message().lower() == 'stop':
    #     print(get_last_message().lower())
    #     send_stop_message()
    #     scheduler.pause()
    #     return

    global movie_date
    current_bot_updates = get_update_counts()
    if current_bot_updates != last_bot_updates:
        movie_date = get_user_message()

    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date="+movie_date
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    movie_list = soup.select('div.col-times')
    imax_movie_list = get_imax_movies(movie_list)
    
    if imax_movie_list:
        if current_date == movie_date:
            current_message = "오늘"
        else:
            current_message = movie_date+"에"
        
        current_message += " IMAX 예매가 열리는 영화는 "+', '.join(imax_movie_list)+"입니다!"
        send_bot_message(current_message)
    else:
        send_bot_message(movie_date+" 에 오픈되는 IMAX 영화가 없습니다.")
        scheduler.pause()
        return

scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', seconds=30)
scheduler.start()