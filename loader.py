from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
owners = [1398970762, 5468103565, 455865567, 2121859796, 5510543158, 5739680333]
