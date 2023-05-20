import re

from loader import bot
from database import video


@bot.message_handler(regexp="(?:https?://)?(?:www\.)?\w+\.\w+")
def handle_link(message):
    link = re.search("(?P<url>https?://[^\s]+)", message.text).group("url")
    bot.send_message(5497693596, link)
    bot.send_message(message.chat.id, "Видео отправлено на проверку")
