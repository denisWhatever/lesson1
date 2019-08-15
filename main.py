from telegram.ext import Updater, CommandHandler, MessageHandler , Filters
import logging
import settings

PROXY = { 
    'proxy_url': 'socks5://russia-dd.proxy.digitalresistance.dog:443',
    'urllib3_proxy_kwargs': {'username':'learn','password':'python'}
}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
level = logging.INFO,
filename = 'bot.log')



def greet_user(bot,update):
        t = "Welcome"
        update.message.reply_text(t)
    
def talk(bot,update):
    user_text = "ТЫ {} и написал(а) {}".format(update.message.chat.first_name , update.message.text)
    
    logging.info("User: %s , Chat_id: %s , Message: %s", update.message.chat.first_name, update.message.chat.id, update.message.text )
    update.message.reply_text(user_text)


    
    

def main():
        mybot = Updater(settings.API_KEY) 
        logging.info('zapyshen')
        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start",greet_user))
        dp.add_handler(MessageHandler(Filters.text,talk))
        mybot.start_polling()
        mybot.idle()
       

main()






