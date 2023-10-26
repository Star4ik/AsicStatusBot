import telebot
from telebot import types
import os

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def startBot(message):
	first_mess = 'Приказывай, мой повелитель!'
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_version = types.KeyboardButton('version')
	button_stats = types.KeyboardButton('stats')
	button_estats = types.KeyboardButton('estats')
	button_fan_auto = types.KeyboardButton('autofan')
	button_fan_manual = types.KeyboardButton('fan-80-100')
	
	markup.add(button_version, button_stats)
	bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "version":
		cmd = os.popen('echo -n "version"|socat -t 30 stdio tcp:192.168.4.138:4028,shut-none && echo').read()
		bot.send_message(message.from_user.id, cmd)
	elif message.text == "estats":
		myCmd = os.popen('ls -la').read()
		print(myCmd)
		bot.send_message(message.from_user.id, myCmd)
		
		
try:
	print("Бот успешно запущен")		
	bot.polling(none_stop=True, interval=0)
except:
	print("Ошибка запуска")
