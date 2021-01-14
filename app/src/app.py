from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import yaml, logging, os, time, requests, json, random

""" Variable Semaforo Estados en la Conversacion """
INPUT_TEXT = 0 

""" Funciones """
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('¡Bienvenido al Actualizador de Compromisos %s!' % update.message.from_user.name)
def chiste(update, context):
    logger.info('Consultando API Frases de Maradona')
    update.message.reply_text(get_frase())
def get_frase():
    num = get_random()
    print ("El random es: % d" % num)
    joke=requests.get('http://api-service:5000/frase/%s' % num)
    data=joke.json()
    return data['frases'][0]['frase']
def get_random():
    cantidad=requests.get('http://api-service:5000/cantidad')
    cant_json = cantidad.json()
    num = cant_json['filas'][0]['COUNT(*)']
    random.randint(0, num)
    return (random.randint(1, num))

""" Main del Programa """
if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('nAutomaticBot')

    """ Llave API para conectarse a Telegram """
    updater = Updater(token="1339119499:AAG7CotDaQcPYnAIS3vR7A70qIQcSa_CbCY", use_context=True)
    dp = updater.dispatcher

    """ Handler's """
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('frase', chiste))


    updater.start_polling()
    updater.idle()
