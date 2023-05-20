from telebot import types

def adm():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Не проверенные видео")
    btn2 = types.KeyboardButton("На главную")
    keyboard.add(btn1, btn2)
    return keyboard
