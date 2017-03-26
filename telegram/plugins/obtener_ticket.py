# -*- coding: utf-8 -*-
#!/usr/bin/python
import time;

# ////// JSON ENDOPOINT //////////////////////

response_tickets = requests.get('http://localhost:8000/api/connections/tickets/?page=1')
tickets = json.loads(response_tickets.text)

response_sucursales = requests.get('http://localhost:8000/api/connections/sucursales/?page=1')
sucursales = json.loads(response_sucursales.text)
print(sucursales)

# ////// JSON ENDOPOINT //////////////////////

#///////////////// PAYMENT //////////

var_sucursarl = None

billing_dict = {}

class Billing:
    def __init__(self, service):
        self.service = service
        self.bank = None
        self.rode = None
        self.card = None
        self.total = None

#///////////////// PAYMENT //////////


@bot.message_handler(commands=['ocultar_teclado'])
def command_hide_board(m):
  try:
    cid = m.chat.id
    bot.send_message(cid, 'Teclado encondido /mostrar_teclado para activar', reply_markup=types.ReplyKeyboardHide())
  except Exception as e:
    bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.message_handler(commands=['mostrar_teclado'])
def command_show_hideboard(m):
  try:
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, 'Teclado activado 🤖', reply_markup=keyboard_options)
  except Exception as e:
    bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def command_options(call):
  try:
    cid = call.message.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)
    bot.send_message(cid, 'typing', reply_markup=types.ReplyKeyboardHide())
  except Exception as e:
    bot.send_message(cid,'🤖', 'Disculpa estoy algo lento intenta otraves!')


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '✅ MENU DE OPCIONES'])
@bot.message_handler(commands=['menu'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, " 🤖 Tienes estas opciones", reply_markup=keyboard_options)



# @bot.message_handler(
#   func=lambda m: m.content_type == 'text' and m.text in [
#       '🏦 VER SUCURSALES'])
# @bot.message_handler(commands=['sucursales'])
# def command_menu(m):
#     cid = m.chat.id
#     bot.send_chat_action(cid, 'typing')
#     keyboard_sucursales = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for sucursal in sucursales:
#         keyboard_sucursales.row(types.KeyboardButton((sucursal["name"])))
#     keyboard_sucursales.add(types.KeyboardButton("❎ CANCELAR"))
#     bot.send_message(cid, " 🤖 Lista de Sucursales", reply_markup=keyboard_sucursales)


#////////////////// LISTAR SUCURSALES /////////////////

def create_calendar(button_1):
    markup = types.InlineKeyboardMarkup()
    row=[]
    row.append(types.InlineKeyboardButton("💧 AGUA",callback_data="ignore"))
    markup.row(*row)
    row=[]
    row.append(types.InlineKeyboardButton("<",callback_data="previous-month"))
    row.append(types.InlineKeyboardButton("USAR",callback_data="ignore"))
    row.append(types.InlineKeyboardButton(">",callback_data="next-month"))
    markup.row(*row)
    return markup


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '🏦 VER SUCURSALES'])
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    cid = message.chat.id
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("boton")
    markup= create_calendar(button_1)
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, "🤖 Tus servicios disponibles", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'next-month')
def next_month(call):
    cid = call.message.chat.id
    markup1 = types.InlineKeyboardMarkup()
    button_2 = types.InlineKeyboardButton("AGENCIA BUSCH",callback_data="ignore")
    button_previous = types.InlineKeyboardButton("<",callback_data="previous-month")
    button_ignore = types.InlineKeyboardButton("USAR",callback_data="ignore")
    button_next = types.InlineKeyboardButton(">",callback_data="next-month")
    markup1.add(button_2)
    markup1.row(button_previous,button_ignore,button_next)
    bot.send_chat_action(cid, 'typing')
    bot.edit_message_text("🤖 Tus servicios disponibles",call.from_user.id, call.message.message_id, reply_markup=markup1)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'previous-month')
def next_month(call):
    cid = call.message.chat.id
    markup1 = types.InlineKeyboardMarkup()
    button_2 = types.InlineKeyboardButton("AGENCIA 7 CALLES",callback_data="ignore")
    button_previous = types.InlineKeyboardButton("<",callback_data="previous-month")
    button_ignore = types.InlineKeyboardButton("USAR",callback_data="ignore")
    button_next = types.InlineKeyboardButton(">",callback_data="next-month")
    markup1.add(button_2)
    markup1.row(button_previous,button_ignore,button_next)
    bot.send_chat_action(cid, 'typing')
    bot.edit_message_text("🤖 Tus servicios disponibles",call.from_user.id, call.message.message_id, reply_markup=markup1)
    bot.answer_callback_query(call.id, text="")


#///////////////// END LISTAR BANCOS /////////////////
@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📑 OBTENER TICKET'])
@bot.message_handler(commands=['obtener_ticket'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid,message_ticket['mensaje_ticket'], reply_markup=keyboard_ubication)


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '📑 ENVIAR UBICACION'])
@bot.message_handler(commands=['ubication'])
def command_menu(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_location(cid,-16.540763, -68.082908,reply_markup=types.ReplyKeyboardHide())
    bot.send_message(cid,"Gracias ya tenemos tu direccion,\n ahora elige el tipo el tipo de ticket ",reply_markup=keyboard_ticket_generate)


@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '🛅 CAJA'])
@bot.message_handler(commands=['generate'])
def process_caja(m):
    cid = m.chat.id
    username = m.from_user.first_name
    localtime = time.asctime( time.localtime(time.time()) )
    timess = time.strftime("%H:%M:%S")

    print("Local current time :", localtime)
    bot.send_message(cid, '🤖 {} Gracias por sacar el ticket,'.format(username) + 
                                  '\n Tu numero de ficha : ' + "C007"+
                                  '\n Tipo de Ficha : ' + "CAJA" +
                                  '\n Hora generada de Ficha  :' + str(timess)
                      )
    bot.send_chat_action(cid,'typing')
    bot.send_photo(cid,open('./telegram/media/tickets/caja.png', 'rb'),reply_markup=types.ReplyKeyboardHide())
    bot.send_message(cid, '🤖 Genial\n ya tienes tu ticket reservado ... ')



@bot.message_handler(
  func=lambda m: m.content_type == 'text' and m.text in [
      '🛃 PLATAFORMA'])
@bot.message_handler(commands=['plataforma'])
def process_plataforma(m):
    cid = m.chat.id
    username = m.from_user.first_name
    localtime = time.asctime( time.localtime(time.time()) )
    timess = time.strftime("%H:%M:%S")

    print("Local current time :", localtime)
    bot.send_message(cid, '🤖 {} Gracias por sacar el ticket,'.format(username) + 
                                  '\n Tu numero de ficha : ' + "P012"+
                                  '\n Tipo de Ficha : ' + "PLATAFORMA" +
                                  '\n Hora generada de Ficha  :' + str(timess)
                      )
    bot.send_chat_action(cid,'typing')
    bot.send_photo(cid,open('./telegram/media/tickets/plataforma.png', 'rb'),reply_markup=types.ReplyKeyboardHide())
    bot.send_message(cid, '🤖 Genial\n ya tienes tu ticket reservado... ')
