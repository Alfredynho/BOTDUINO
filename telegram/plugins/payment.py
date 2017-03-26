# # -*- coding: utf-8 -*-
# from config import *


# # ////// JSON ENDOPOINT //////////////////////
# response = requests.get('http://localhost:8000/api/connections/services/')
# services = json.loads(response.text)

# response_card = requests.get('http://localhost:8000/api/connections/banks/?page=1')
# banks = json.loads(response_card.text)


# # ////// JSON ENDOPOINT //////////////////////

# #///////////////// PAYMENT //////////

# billing_dict = {}

# class Billing:
#     def __init__(self, service):
#         self.service = service
#         self.bank = None
#         self.rode = None
#         self.card = None
#         self.total = None


# #///////////////// PAYMENT //////////


# @bot.message_handler(commands=['ocultar_teclado'])
# def command_hide_board(m):
#   try:
#     cid = m.chat.id
#     bot.send_message(cid, 'Teclado encondido /mostrar_teclado para activar', reply_markup=types.ReplyKeyboardHide())
#   except Exception as e:
#     bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


# @bot.message_handler(commands=['mostrar_teclado'])
# def command_show_hideboard(m):
#   try:
#     cid = m.chat.id
#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid, 'Teclado activado 🤖', reply_markup=keyboard_options)
#   except Exception as e:
#     bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


# @bot.callback_query_handler(func=lambda call: call.data == 'menu')
# def command_options(call):
#   try:
#     cid = call.message.chat.id
#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)
#     bot.send_message(cid, 'typing', reply_markup=types.ReplyKeyboardHide())
#   except Exception as e:
#     bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


# @bot.message_handler(
#   func=lambda m: m.content_type == 'text' and m.text in [
#       '✅ MENU DE OPCIONES'])
# @bot.message_handler(commands=['menu'])
# def command_menu(m):
#     cid = m.chat.id
#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)


# @bot.message_handler(
#     func=lambda m: m.content_type == 'text' and m.text in [
#         '💵 SERVICIOS DE CHUSPITABOT'])
# @bot.message_handler(commands=['pagar_servicios'])
# def command_payment(m):

#     keyboard_services = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for service in services:
#         keyboard_services.row(types.KeyboardButton((service["type"])))    
#     keyboard_services.add(types.KeyboardButton("📲 SERVICIO DE RECARGA"))
#     keyboard_services.add(types.KeyboardButton("❎ CANCELAR"))

#     cid = m.chat.id
#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid, " 🤖 Tienes los siguientes servicios disponibles", reply_markup=keyboard_services)

# @bot.message_handler(
#   func=lambda m: m.content_type == 'text' and m.text in [
#       'AGUA'])

# @bot.message_handler(commands=['agua'])
# def command_payment_services(m):
#     cid = m.chat.id
#     select_service = m.text
#     billing = Billing(select_service)
#     billing_dict[cid] = billing
#     billing.service = select_service

#     print("PRINTEO Service",billing.service)

#     keyboard_cards = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for card in banks:
#         keyboard_cards.row(types.KeyboardButton((card["name"])))
#     keyboard_cards.add(types.KeyboardButton("❎ CANCELAR"))

#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid, " 🤖 Tienes los siguientes tarjetas disponibles", reply_markup=keyboard_cards)


# def create_detail(button_1,cid):

#     markup = types.InlineKeyboardMarkup()
#     row=[]
#     bot.send_message(cid,'🤖 Generando detalle de pago ... ',reply_markup=types.ReplyKeyboardHide())
#     bot.send_chat_action(cid, 'typing')
#     bot.send_message(cid,
#                      ("⚠ Atencion ⚠\n"
#                       " 🤖 Ok, Usted realizara el pago de 300 Bs\n"
#                       "al servicio de EPSAS con su tarjeta BNB\n"
#                       "Desea proseguir con el pago? "
#                       ),
#                      disable_web_page_preview=True,
#                      parse_mode="Markdown")

#     row.append(types.InlineKeyboardButton("☑ CONTINUAR",callback_data="continuar"))
#     row.append(types.InlineKeyboardButton("✖ CANCELAR",callback_data="cancelar"))
#     markup.row(*row)
#     return markup

# current_shown_dates={}

# @bot.message_handler(
#   func=lambda m: m.content_type == 'text' and m.text in [
#       'BANCO UNION'])
# @bot.message_handler(commands=['union'])
# def get_options(message):
#     cid = message.chat.id
#     select_card = message.text
#     billing = Billing(select_card)
#     billing_dict[cid] = billing
#     billing.card = select_card

#     print("PRINTEO card",billing.card)

#     current_shown_dates[cid] = cid
#     markup = types.InlineKeyboardMarkup()
#     button_1 = types.InlineKeyboardButton("boton")
#     markup= create_detail(button_1,cid)
#     bot.send_message(cid, "🤖 Tienes las siguientes opciones ", reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: call.data == 'continuar')
# def next_keyboard(call):
#     cid = call.message.chat.id
#     markup1 = types.InlineKeyboardMarkup()
#     button_previous = types.InlineKeyboardButton("🔑 OBTENER TOKEN",callback_data="token")
#     button_ignore = types.InlineKeyboardButton("❓ COMO OBTENER",url="https://chuspita.net/get_token")
#     button_next = types.InlineKeyboardButton("✖ CANCELAR",callback_data="cancelar")
#     markup1.add(button_previous)
#     markup1.row(button_ignore,button_next)
#     bot.edit_message_text("🤖 Que deseas realizar ?",call.from_user.id, call.message.message_id, reply_markup=markup1)
#     bot.answer_callback_query(call.id, text="")

# @bot.callback_query_handler(func=lambda call: call.data == 'cancelar')
# def previous_keyboard(call):
#     cid = call.message.chat.id
#     markup1 = types.InlineKeyboardMarkup()
#     button_ignore = types.ReplyKeyboardMarkup("🤖 Quieres volver al menu ? ",callback_data="pagar_servicios")
#     markup1.row(button_ignore)
#     bot.edit_message_text("🤖 pulsaste cancelar ",call.from_user.id, call.message.message_id, reply_markup=markup1)
#     bot.answer_callback_query(call.id, text="")

# @bot.callback_query_handler(func=lambda call: call.data == 'token')
# def view_token(call):
#     cid = call.message.chat.id
#     markup1 = types.InlineKeyboardMarkup()
#     bot.send_chat_action(cid, 'typing')
#     bot.edit_message_text('🤖 Segerencia\n Debes ir a la app Chuspita\n generar tu token,\n luego pegarlo aqui ',call.from_user.id, call.message.message_id)
#     bot.answer_callback_query(call.id, text="")

#     keyboard_token = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_token = types.KeyboardButton('🔑 CONTINUAR ⤵')
#     keyboard_token.add(button_token)
#     bot.send_message(cid,'🤖 Pulse continuar',reply_markup=keyboard_token)

# @bot.message_handler(
#   func=lambda m: m.content_type == 'text' and m.text in [
#       '🔑 CONTINUAR ⤵'])
# @bot.message_handler(commands=['token_payment'])
# def get_options(message):
#     try:
#         cid = message.chat.id
#         msg = bot.reply_to(message, '🤖 Puedes ingresar tu token aqui porfavor',reply_markup=types.ReplyKeyboardHide())
#         bot.register_next_step_handler(msg, process_age_step)
#     except Exception as e:
#         bot.reply_to(message, '🤖 oooops1')

# def process_age_step(message):

#     cid = message.chat.id
#     username = message.from_user.first_name
#     age = message.text
#     respuesta = message.text
#     billing = billing_dict[cid]
#     if not age.isdigit():
#         msg = bot.reply_to(message, '🤖 El Token que ingresaste es erroneo\n intenta otravez')
#         bot.register_next_step_handler(msg, process_age_step)
#         return
#     monto = 300
#     total = 302
#     bot.reply_to(message, '🤖 Un placer \n atenderte {},'.format(username) + 
#                                   '\n Servicio pagado : ' + "AGUA" +
#                                   '\n Servicio pagado : ' + billing.card +
#                                   '\n Monto :' + str(monto) +
#                                   '\n Total ' + str(total) 
#                       )
#     bot.send_message(cid,'🤖 Quieres descargar el detalle ?',reply_markup=keyboard_detail)
