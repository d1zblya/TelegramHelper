import telebot
from telebot import types

bot = telebot.TeleBot('6565535745:AAFQ7CprBwnO8USfqPiVBg-oWNsC-Si01iA')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Метод рационализации')
    btn2 = types.KeyboardButton('Метод переброски коэффициентов')
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton('Расстояние между точками')
    btn4 = types.KeyboardButton('Вычисление логарифма')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! '
                                      f'Выбери то, что тебя интересует', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Метод рационализации':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Мне нравится 👍')
        btn2 = types.KeyboardButton('Мне не нравится 👎  ')
        back = types.KeyboardButton('Вернуться назад')
        markup.row(btn2, btn1)
        markup.row(back)
        file1 = open('Photos/file1.png', 'rb')
        bot.send_photo(message.chat.id, file1, reply_markup=markup)
    elif message.text == 'Метод переброски коэффициентов':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Мне нравится 👍')
        btn2 = types.KeyboardButton('Мне не нравится 👎')
        back = types.KeyboardButton('Вернуться назад')
        markup.row(btn2, btn1)
        markup.row(back)
        file2 = open('Photos/file2.png', 'rb')
        bot.send_photo(message.chat.id, file2, reply_markup=markup)
    elif message.text == 'Расстояние между точками':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Мне нравится 👍')
        btn2 = types.KeyboardButton('Мне не нравится 👎')
        back = types.KeyboardButton('Вернуться назад')
        markup.row(btn2, btn1)
        markup.row(back)
        file3 = open('Photos/file3.png', 'rb')
        bot.send_photo(message.chat.id, file3, reply_markup=markup)
    elif message.text == 'Вычисление логарифма':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Мне нравится 👍')
        btn2 = types.KeyboardButton('Мне не нравится 👎')
        back = types.KeyboardButton('Вернуться назад')
        markup.row(btn2, btn1)
        markup.row(back)
        file4 = open('Photos/file4.png', 'rb')
        bot.send_photo(message.chat.id, file4, reply_markup=markup)
    elif message.text == 'Мне нравится 👍':
        bot.reply_to(message, 'Очень рад вам помочь! 😊')
    elif message.text == 'Мне не нравится 👎':
        bot.reply_to(message, 'Очень жаль 😢')
    elif message.text == 'Вернуться назад':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Метод рационализации')
        btn2 = types.KeyboardButton('Метод переброски коэффициентов')
        markup.row(btn1, btn2)
        btn3 = types.KeyboardButton('Расстояние между точками')
        btn4 = types.KeyboardButton('Вычисление логарифма')
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=markup)


bot.polling(none_stop=True)

# sdfsdfsdfsd
# sdfsdfsdfsd
# sdfsdfsdfsd
# sdfsdfsdf
# 3 fidfhwwidfiwfffffffwihfiwhfiwfwf



