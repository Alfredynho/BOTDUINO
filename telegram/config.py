# # -*- coding: utf-8 -*-
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# import requests
# import telebot
# from telebot import types
# from colorclass import Color
# from colorclass import disable_all_colors, enable_all_colors, is_enabled
# from colorclass import set_dark_background, set_light_background
# from colorclass import Windows
# import json
# import time
# import six
# import sys
# import traceback
# import re
# import socket

# from os.path import join, dirname
# import sys, os, environ
# from django.conf import settings
# from django import setup


# chatbot = ChatBot("Charlie")

# response = chatbot.get_response("How are you?")

# print(response)

# def config_django():
#     PROJECT_PATH = dirname(dirname(__file__))
#     APPS_PATH = join(PROJECT_PATH, "apps")
#     CONFIG_PATH = join(PROJECT_PATH, "config")
#     TELEGRAM_PATH = join(PROJECT_PATH, "telegram")
#     sys.path.insert(0, PROJECT_PATH)
#     sys.path.insert(0, APPS_PATH)
#     sys.path.insert(0, CONFIG_PATH)
#     sys.path.insert(0, TELEGRAM_PATH)
#     env = environ.Env()
#     env.read_env(".environment")
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
#     settings.DATABASES["default"] = env.db("DATABASE_URL")
#     setup()

# #Token chuspitaBOT
# bot = telebot.TeleBot('274345964:AAFb-_bvTqETeLdX6rxL2miSi5yDZCWZKrA')
