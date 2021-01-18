from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import yaml, logging, os, time, requests, json, random

""" Variable Semaforo Estados en la Conversacion """
INPUT_TEXT = 0 

""" Funciones """
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('¡Bienvenido al BOT del D10s %s, ahora vas a tener sus mejores frases, junto a vos!' % update.message.from_user.name)
def frase(update, context):
    logger.info('Consultando API Frases de Maradona')
    update.message.reply_text(get_frase())
def get_frase():
    num = get_random()
    joke=requests.get('http://api-service:5000/frase/%s' % num)
    data=joke.json()
    msg = "Frase: %s \n" % data['frases'][0]['frase']
    msg = msg + "Detalle: %s" % data['frases'][0]['detalle']
    return msg

def get_random():
    cantidad=requests.get('http://api-service:5000/cantidad')
    cant_json = cantidad.json()
    num = cant_json['filas'][0]['COUNT(*)']
    random.randint(0, num)
    return (random.randint(1, num))

""" Main del Programa """
if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('El Bot de D10S')

    """ Llave API para conectarse a Telegram """
    updater = Updater(token=os.getenv("TOKEN_TELEGRAM"), use_context=True)
    dp = updater.dispatcher

    """ Handler's """
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('frase', frase))


    updater.start_polling()
    updater.idle()
