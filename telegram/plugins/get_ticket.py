# -*- coding: utf-8 -*-


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📑 RESERVAR TICKET'])
@bot.message_handler(commands=['reservar_ticket'])
def command_ticket(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,"🤖 Debes elegir un Banco ",reply_markup=keyboard_cards)


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💳 TARJETA UNION'])
@bot.message_handler(commands=['tarjeta_union'])
def command_banks(m):
    try:
        cid = m.chat.id
        button_ubication = types.ReplyKeyboardMarkup(resize_keyboard= True)
        button_ubication.add(types.KeyboardButton("📌 ENVIAR UBICACION"))
        bot.send_chat_action(cid, 'typing')
        msg = bot.reply_to(m, '🤖 Para enviar \n presiona Enviar Ubicacion',reply_markup=button_ubication)
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(m, '🤖 oooops1')

def process_age_step(message):
    cid = message.chat.id
    username = message.from_user.first_name
    age = message.text
    bot.send_message(cid,'🤖 mensaje !!!')
