import telebot
from telebot import types  # для указание типо


def lab2():
    names = []
    bot = telebot.TeleBot('5938392811:AAExt8kq30g_MWyxioRLTq1u96iQJyhw1XY')  # токен бота

    @bot.message_handler(commands=['start'])
    def start(message):
        next = bot.send_message(message.chat.id, "Здравствуйте! Для того, чтобы начать запись, введите"
                                                 " Ваше ФИО через пробел.", parse_mode='html')
        bot.register_next_step_handler(next, choose_type)

    def choose_type(message):
        FIO = message.text
        names.append(FIO)

        markup = types.InlineKeyboardMarkup(row_width=1)

        button1 = types.InlineKeyboardButton('Полумарафон (21 км 97,5 м.)',
                                             callback_data='but1')
        button2 = types.InlineKeyboardButton('Марафон (классический) (42 км 195 м.)',
                                             callback_data='but2')
        button3 = types.InlineKeyboardButton('Ультрамарафон (50 до 100 км.)',
                                             callback_data='but3')

        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text='На какой вид бегавого марафона Вы бы хотели записаться?',
                         reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.message:
            if call.data == 'but1':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Подтвердить")
                btn2 = types.KeyboardButton("Записаться заново")
                markup.add(btn1, btn2)
                bot.send_message(call.message.chat.id,
                                 text=f"{names[len(names) - 1]}, Вы записаны на полумарафон, который состоится 25.04 в 9:00",
                                 reply_markup=markup)
            if call.data == 'but2':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Подтвердить")
                btn2 = types.KeyboardButton("Записаться заново")
                markup.add(btn1, btn2)
                bot.send_message(call.message.chat.id,
                                 text=f"{names[len(names) - 1]}, Вы записаны на марафон (классический), который состоится 30.04 в 9:00",
                                 reply_markup=markup)
            if call.data == 'but3':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Подтвердить")
                btn2 = types.KeyboardButton("Записаться заново")
                markup.add(btn1, btn2)
                bot.send_message(call.message.chat.id,
                                 text=f"{names[len(names) - 1]}, Вы записаны на ультрамарафон, который состоится 05.05 в 9:00",
                                 reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def confirm(message):
        delete = telebot.types.ReplyKeyboardRemove()
        if message.text == "Подтвердить":
            bot.send_message(message.chat.id, "Отлично! Будем Вас ждать.", reply_markup=delete)
        elif message.text == "Записаться заново":
            bot.send_message(message.chat.id, "Новая запись", reply_markup=delete)
            names.clear()
            next = bot.send_message(message.chat.id, "Здравствуйте! Для того, чтобы начать запись, введите"
                                                     " Ваше ФИО через пробел.", parse_mode='html')
            bot.register_next_step_handler(next, choose_type)

    bot.polling(none_stop=True)
