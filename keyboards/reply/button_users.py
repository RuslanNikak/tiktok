from telebot import types

def users():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Моя статистика")
    btn2 = types.KeyboardButton("Связаться с админами")
    keyboard.add(btn1, btn2)
    return keyboard

def statistik():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Мои последние 5 видео")
    btn2 = types.KeyboardButton("Все видео")
    btn3 = types.KeyboardButton("Информация о всех видео")
    btn4 = types.KeyboardButton("На главную")
    keyboard.add(btn1, btn2, btn3, btn4)
    return keyboard

def stat():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("На главную")
    keyboard.add(btn1)
    return keyboard