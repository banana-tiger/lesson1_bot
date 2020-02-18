from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("1059535934:AAEogOPYQZ3fAA2u5VCoOWRMJdDCFe-PciU", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, greet_user))
    dp.add_handler(MessageHandler(Filters.sticker, top_kek))

    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'кек'
    print(text)
    update.message.reply_text(text)

def top_kek(bot, update):
    text = 'ну просто топ кек'
    print(text)
    update.message.reply_text(text)

main()
