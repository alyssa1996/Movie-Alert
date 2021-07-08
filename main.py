from re import S
from movie_crawler import check_movie_list, run_crawler
from datetime import datetime
from telegram_message import *
from apscheduler.schedulers.blocking import BlockingScheduler

last_bot_updates = get_update_counts()

def start_job():
    movie_date = datetime.now().strftime('%Y%m%d')
    current_bot_updates = get_update_counts()
    if current_bot_updates != last_bot_updates:
        movie_date = get_user_message()

    imax_movie_list = run_crawler(movie_date)
    if not check_movie_list(imax_movie_list, movie_date):
        add_message = '\n 다른 날짜의 IMAX 오픈 영화를 알고 싶다면 YYYYMMDD 형태로 날짜를 입력해주세요!'
        send_bot_message(movie_date+" 에 오픈되는 IMAX 영화가 없습니다."+add_message)

def job_function():
    print(get_last_message())
    if get_last_message().lower() == 'stop':
        scheduler.remove_job('job_1')
    else:
        print('start job')
        start_job()

scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', seconds=30, id='job_1')
scheduler.start()