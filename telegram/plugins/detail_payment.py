
@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📥 DESCARGAR'])
@bot.message_handler(commands=['download'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_document(cid, open('./telegram/media/Bancobnb.jpg', 'rb'), reply_markup=types.ReplyKeyboardHide())
    bot.send_message(cid,'🤖 Un gusto atenderte ...')


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '↗ IR A INICIO'])
@bot.message_handler(commands=['home'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '💳 TARJETA BNB'])
@bot.message_handler(commands=['home'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)

