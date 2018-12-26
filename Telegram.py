#!/usr/bin/python3.6
#! _*_ coding: UTF-8 _*_

import telebot
from datetime import datetime, timedelta
import requests
import json
import os
import zipfile
import time
import tempfile
from telebot import apihelper
import time


CURR_DIR = os.path.dirname(os.path.abspath(__file__))

#import logging

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)
#_______
#string3 = 'https://mike007:R7i7YbE@91.211.88.155:65233'

token = '701051245:AAGg_DAM7m5oJMozYOksJZ3Cp9e8GQIHaAI'
bot = telebot.TeleBot(token=token)
#apihelper.proxy = {'https':string3,'http':string3}

apihelper.proxy = {'https':'socks5://lanproxyuser2:TXzhsh6LE7@internal.fintechcrm.ru:1080'}

users = [326404173,235794451,323434566,446588133,444967002,186509669] 
# i'm, plan,elka,dimon,andy, @MikleStepanov
# bot_accounts = ['blm','Elka','dispell','Andy_blm_shared']


def ziping(tmpfile_name = 'tmpfile.zip'):
	try:
		p = r'..//'
		F = []
		for i in os.listdir(p):
			try:
				F.extend([os.path.abspath(p + i + '\\' +  s) for s 
					in os.listdir(p + i) if s.endswith('.log')])
			except Exception:
				pass
		Z = zipfile.ZipFile(tmpfile_name, 'w')
		for f in F:
		    Z.write(f)
		Z.close()
	except Exception as err:
		tmpfile_name = 'Error: \n %s'%err
	return tmpfile_name
	if os.path.isfile(tmpfile_name):
		time.sleep(1)
		os.remove(tmpfile_name)

def ziping_all_log(tmpfile_name = 'tmpfile.zip'):
	try:
		p = r'..//'
		F = []
		for root, dirs, files in os.walk(p):
			for f in [s for s in files if s.find('.log') != -1]:
				F.append(os.path.abspath(root +'\\' + f))
		Z = zipfile.ZipFile(tmpfile_name, 'w')
		for f in F:
		    Z.write(f)
		Z.close()
	except Exception as err:
		tmpfile_name = 'Error: \n %s'%err
	return tmpfile_name



	# shutil.copy2('tmpfile', r'D:\blm\1ARRRRRRHIV.zip')



@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Получить логи', 'Получить ВСЕ логи')
    bot.send_message(message.chat.id,'НажЫмай', reply_markup=user_markup)
    print(message)



@bot.message_handler(content_types=['text'])
def handle_start(message):
	if list(filter(lambda x: x == message.chat.id, users)) != []:
		try:
			if message.text == 'Получить логи':
				user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
				user_markup.row('/start')
				tmpfile_name = 'tmpfile.zip'
				if os.path.isfile(tmpfile_name):
					os.remove(tmpfile_name)
				zfile = ziping(tmpfile_name)
				if zfile.startswith('Error'):
					bot.send_message(message.chat.id, zfile, reply_markup=user_markup)
				else:
					doc = open(tmpfile_name, 'rb')
					bot.send_document(message.chat.id, doc)

			if message.text == 'Получить ВСЕ логи':
				user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
				user_markup.row('/start')
				tmpfile_name = 'tmpfile2.zip'
				if os.path.isfile(tmpfile_name):
					os.remove(tmpfile_name)
				zfile = ziping_all_log(tmpfile_name)
				if zfile.startswith('Error'):
					bot.send_message(message.chat.id, zfile, reply_markup=user_markup)
				else:
					doc = open(tmpfile_name, 'rb')
					bot.send_document(message.chat.id, doc)


		except Exception as err:
			print('!!!!!ERROORR',err)
	else:
		bot.send_message(message.chat.id, 'Бот в разработке. Для доступа обратитесь @blm47\n Ваш id: %s'%message.chat.id)
		print(message)


def start_polling():
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        time.sleep(23)
        start_polling()
        print(err)

if __name__ == "__main__":
    start_polling()
