from telegram.ext import Updater, Filters
import yaml, logging, os, time, requests, json, random, schedule, telegram

""" Variables """
token = os.getenv("TOKEN_TELEGRAM")
chat_id = os.getenv("CHAT_ID")


""" Funciones """
def get_frase():
    num = get_random()
    joke=requests.get('http://api-service:5000/frase/%s' % num)
    data=joke.json()
    msg = "Frase: %s \n" % data['frases'][0]['frase']
    msg = msg + "Detalle: %s" % data['frases'][0]['detalle']
    return msg

def send_message(token, chat_id, msg):
    logger.info('Consultando API Frases de Maradona')
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=msg)
            
def get_random():
    cantidad=requests.get('http://api-service:5000/cantidad')
    cant_json = cantidad.json()
    num = cant_json['filas'][0]['COUNT(*)']
    random.randint(0, num)
    return (random.randint(1, num))

""" Logging """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('BOT de D10S')
logging.getLogger('schedule').setLevel(logging.CRITICAL + 10)
logger.info('······ WELCOME TO MARADONA BOT ······')

""" Setting Time """
schedule.every(3).minutes.do(send_message, token, chat_id, get_frase())


while True:
    schedule.run_pending()
    time.sleep(30)
