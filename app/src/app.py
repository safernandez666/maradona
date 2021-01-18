from telegram.ext import Updater, Filters
import yaml, logging, os, time, requests, json, random, schedule, telegram

""" Variables """
token = os.getenv("TOKEN_TELEGRAM")
chat_id = os.getenv("CHAT_ID")
minutes = os.getenv("MINUTES")

""" Funciones """
def send_message():
    num = get_random()
    joke=requests.get('http://api-service:5000/frase/%s' % num)
    data=joke.json()
    msg = "Frase: %s \n" % data['frases'][0]['frase']
    msg = msg + "Detalle: %s" % data['frases'][0]['detalle']
    logger.info('···· SE ENVIO EL MENSAJE A TELGRAM ····')
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=msg)
            
def get_random():
    cantidad=requests.get('http://api-service:5000/cantidad')
    cant_json = cantidad.json()
    num = cant_json['filas'][0]['COUNT(*)']
    logger.info('······ SE CONSULTA CANTIDAD: %d ······' % num)
    ran = random.randint(1, num)
    logger.info('······ INGRESO A RANDOM ES: %d ······' % ran)
    return (ran)

""" Logging """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('BOT de D10S')
logging.getLogger('schedule').setLevel(logging.CRITICAL + 10)
logger.info('······ WELCOME TO MARADONA BOT ······')

""" Setting Time """
schedule.every(1).minutes.do(send_message)


while True:
    schedule.run_pending()
    time.sleep(30)