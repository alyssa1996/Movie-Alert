import telegram
import telegram_bot

bot = telegram.Bot(token=telegram_bot.getToken())

def get_update_counts():
    return len(list(bot.getUpdates()))

def get_user_message():
    update_info = bot.getUpdates()[-1].message
    date = update_info.text
    return date

def get_last_message():
    return bot.getUpdates()[-1].message.text

def send_stop_message():
    return bot.sendMessage(chat_id = telegram_bot.getChatID(), text= "봇 운영을 종료합니다. 감사합니다!")

def send_bot_message(message):
    return bot.sendMessage(chat_id = telegram_bot.getChatID(), text= message)