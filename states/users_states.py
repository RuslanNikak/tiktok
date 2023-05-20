from loader import bot

from telebot.handler_backends import State, StatesGroup
from telebot import custom_filters


class MyStates(StatesGroup):
    user_id = State()
    bot = State()


bot.add_custom_filter(custom_filters.StateFilter(bot))
