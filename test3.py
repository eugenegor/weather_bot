import telebot

bot = telebot.TeleBot("5588632672:AAGP_rxrrA-9cuqdgOA5UD3sO1eZINLW7Bg", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()