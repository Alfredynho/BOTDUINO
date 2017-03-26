
@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        '📲 SERVICIO DE RECARGA'])
@bot.message_handler(commands=['recargar_credito'])
def command_payment(m):
  cid = m.chat.id
  username = m.from_user.first_name
  bot.send_chat_action(cid, 'typing')
  bot.send_message(cid, " 🤖 {} Tienes los , siguientes contactos".format(username), reply_markup=keyboard_contacts)



@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        '👤 73053045'])
def command_payment(m):
  cid = m.chat.id
  username = m.from_user.first_name
  bot.send_chat_action(cid, 'typing')
  bot.send_message(cid, " 🤖 Cuanto deseas recargar?".format(username), reply_markup=keyboard_rode)


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        '💵 30'])
def command_payment(m):
  cid = m.chat.id
  username = m.from_user.first_name
  bot.send_chat_action(cid, 'typing')
  bot.send_message(cid,'🤖 procesando ... ',reply_markup=types.ReplyKeyboardHide())
  bot.send_message(cid, " 🤖 {} Tienes las siguientes opciones ".format(username), reply_markup=keyboard_recarge)
