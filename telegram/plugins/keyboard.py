# -*- coding: utf-8 -*-
#!/usr/bin/python3
# teclados bot
keyboard_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_menu = types.KeyboardButton('✅ MENU DE OPCIONES')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_menu.row(button_menu)
keyboard_menu.add(button_cancel)


keyboard_options = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_ticket = types.KeyboardButton('📑 OBTENER TICKET')
button_my_tickets = types.KeyboardButton('📑 MIS TICKETS')
button_help = types.KeyboardButton('🚀 AYUDA')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_options.row(button_ticket,button_my_tickets)
keyboard_options.add(button_help)
keyboard_options.row(button_cancel)

keyboard_ubication = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_ubication = types.KeyboardButton('📑 ENVIAR UBICACION')
button_sucursales = types.KeyboardButton('🏦 VER SUCURSALES')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_ubication.add(button_ubication,button_sucursales)
keyboard_ubication.row(button_cancel)


options_keyboards1 = types.InlineKeyboardMarkup()
button_home = types.InlineKeyboardButton("☑ INICIO",callback_data="menu")
button_cancel = types.InlineKeyboardButton("✖ CANCELAR",callback_data="cancelar")
options_keyboards1.add(button_home,button_cancel)


options_keyboards2 = types.InlineKeyboardMarkup()
button_continue = types.InlineKeyboardButton("☑ CONTINUAR",callback_data="continuar")
button_cancel = types.InlineKeyboardButton("✖ CANCELAR",callback_data="cancelar")
options_keyboards2.add(button_continue,button_cancel)


# keyboard_sucursales = types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard_sucursales.add(types.KeyboardButton('🏦 CAMACHO'),types.KeyboardButton('🏦 PRADO'))
# keyboard_sucursales.add(types.KeyboardButton('🏦 STADIUM'),types.KeyboardButton('🏦 PEREZ'))
# keyboard_sucursales.row(types.KeyboardButton('❎ CANCELAR'))


keyboard_ticket_generate = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_caja = types.KeyboardButton('🛅 CAJA')
button_plataforma = types.KeyboardButton('🛃 PLATAFORMA')
button_cancel = types.KeyboardButton('❎ CANCELAR')
keyboard_ticket_generate.add(button_caja,button_plataforma)
keyboard_ticket_generate.row(button_cancel)


keyboard_recarge = types.InlineKeyboardMarkup()
button_recarga = types.InlineKeyboardButton("☑ RECARGAR",callback_data="token")
button_cancel = types.InlineKeyboardButton("✖ CANCELAR",callback_data="cancelar")
keyboard_recarge.row(button_recarga,button_cancel)
