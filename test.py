
from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
import telebot


config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('bb745a423261ed0bd4b416152d2b7ef7')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5588632672:AAGP_rxrrA-9cuqdgOA5UD3sO1eZINLW7Bg", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):

    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"
			


			
    bot.send_message(message.chat.id, answer)

bot.infinity_polling()
