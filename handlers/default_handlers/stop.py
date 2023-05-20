from loader import bot


@bot.message_handler(commands=["stop"])
def start(message):
    bot.send_message(message.chat.id, 'Выход произведён')
    bot.delete_state(message.from_user.id, message.chat.id)
