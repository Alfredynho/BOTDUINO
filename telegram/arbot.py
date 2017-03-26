#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging

import requests
import telebot
from telebot import types
from colorclass import Color
from colorclass import disable_all_colors, enable_all_colors, is_enabled
from colorclass import set_dark_background, set_light_background
from colorclass import Windows
import json
import time
import six
import sys
import traceback
import re
import socket

from utils import config_django

bot = telebot.TeleBot('274345964:AAFb-_bvTqETeLdX6rxL2miSi5yDZCWZKrA')

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Cargando plugins...{/cyan}'))

config_django()

keyboard_ubication = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_ubication = types.KeyboardButton('📑 ENVIAR UBICACION')
button_sucursales = types.KeyboardButton('🏦 VER SUCURSALES')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_ubication.add(button_ubication,button_sucursales)
keyboard_ubication.row(button_cancel)

keyboard_options = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_ticket = types.KeyboardButton('📑 OBTENER TICKET')
button_my_tickets = types.KeyboardButton('📑 MIS TICKETS')
button_help = types.KeyboardButton('🚀 AYUDA')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_options.row(button_ticket,button_my_tickets)
keyboard_options.add(button_help)
keyboard_options.row(button_cancel)

from apps.messaging.models import Answer

chuspita = ChatBot("Chupita")
chuspita.set_trainer(ListTrainer)
answers = Answer.objects.all()
for answer in answers:
    item = [answer.question, answer.response]
    chuspita.train(item)


@bot.message_handler(func=lambda message: True)
def information(m):
    cid = m.chat.id
    texto = m.text
    answer = chuspita.get_response(texto)
    print(texto)
    print(answer)
    if answer == "sucursales":
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid,answer,reply_markup=keyboard_options)


try:
    print(Color('    {autogreen}- Iniciando {/red} {autogreen}conexion{/red}'))
    print(Color('    - Conectando con {bgblue}{black}CHUSPITA BOT{/black}{/bgblue} ... [OK] -'))
    print(Color('    - Ctrl + C para detener el Bot'))
    def main_loop():
        bot.polling(True)
        while 1:
            time.sleep(15)
            
    if __name__ == '__main__':
        try:
            main_loop()
        except KeyboardInterrupt:
            print >> sys.stderr, '\nExiting by user request.\n'
            sys.exit(0)

except Exception as e:
    print ("Conectando con Bot de Telegram -> ERROR")
    print (e)
    sys.exit(1)



