#!/usr/bin/python3

@bot.message_handler(commands=['start'])
def welcome(m):
    try:
        cid = m.chat.id
        username = m.from_user.first_name
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid,text_messages['welcome'],reply_markup=types.ReplyKeyboardHide())
        bot.send_message(cid,'Ahora tus pagos son mas faciles!')
        bot.send_message(cid,'🤖 {}, puedes ver las opciones de ChuspitaBOT'.format(username), reply_markup=keyboard_menu)
    except Exception as e:
        bot.reply_to(m,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['❎ CANCELAR'])
def cancel(m):
    cid = m.chat.id
    bot.send_message(cid, " 🤖 /comandos para ver comandos", reply_markup=types.ReplyKeyboardHide())

@bot.message_handler(commands=['informacion'])
def information(m):
    try:
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        bot.send_sticker(cid,'BQADAQADFAADmKNCCdFUpswRw_0lAg',reply_markup=types.ReplyKeyboardHide())
        bot.send_message(cid,text_messages['information'])
    except Exception as e:
        bot.reply_to(m,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.message_handler(commands=['ayuda'])
def help(m):
    try:
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid,text_messages['help'],reply_markup=types.ReplyKeyboardHide())
    except Exception as e:
        bot.reply_to(m,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.message_handler(commands=['comandos'])
def commands(m):
    try:
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid,text_messages['commands'],reply_markup=types.ReplyKeyboardHide())
    except Exception as e:
        bot.reply_to(m,'🤖', 'Disculpa estoy algo lento intenta otraves!')




# --------------- COMANDOS PARA CHUSPITABOT -----------------
# start - Bienvenida de ChuspitaBOT
# menu - Menu de opciones
# obtener_ticket- Realizar el pago de servicios
# ayuda - Ayuda
# ocultar_teclado - Esconder teclado
# mostrar_teclado - mostrar_teclado
# informacion - Informacion de ChuspitaBOT
# -----------------------------------------------------------