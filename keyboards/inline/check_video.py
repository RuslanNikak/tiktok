from telebot import types


def keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("👍", callback_data="1")
    button2 = types.InlineKeyboardButton("👎", callback_data="2")
    markup.add(button1, button2)
    return markup