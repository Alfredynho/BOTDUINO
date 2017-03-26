# -*- coding: utf-8 -*-

@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💡 LUZ'])
@bot.message_handler(commands=['luz'])
def command_light(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['service'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💻 INTERNET'])
@bot.message_handler(commands=['internet'])
def command_internet(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['service'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📡 CABLE'])
@bot.message_handler(commands=['cable'])
def command_cable(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['service'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📞 TELEFONIA'])
@bot.message_handler(commands=['telefonia'])
def command_telephony(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['service'])

@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '❎ CANCELAR'])
@bot.message_handler(commands=['cancelar'])
def command_cancel(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['cancel'], reply_markup=keyboard_options)


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💳 TARJETA BCP'])
@bot.message_handler(commands=['bcp'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['bank'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💳 TARJETA UNION'])
@bot.message_handler(commands=['union'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['bank'])



#///////////////////// MONTOS /////////////////

@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💵 10'])
@bot.message_handler(commands=['monto'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['no_disponible'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💵 20'])
@bot.message_handler(commands=['monto'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['no_disponible'])

@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💵 30'])
@bot.message_handler(commands=['monto'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['no_disponible'])


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💵 40'])
@bot.message_handler(commands=['monto'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['no_disponible'])



#////////////////////////MONTOS /////////////////////////



#/////////////////////// CONTACTS///////////////////////////


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💵 40'])
@bot.message_handler(commands=['monto'])
def command_null_card(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,text_messages_error['no_disponible'])
