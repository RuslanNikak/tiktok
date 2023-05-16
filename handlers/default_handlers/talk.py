from loader import bot
from states.users_states import MyStates


@bot.message_handler(state=MyStates.user_id, content_types=["text"])
def talk_admins(message):
    if message.text:
        bot.forward_message(-880322702, message.from_user.id, message.message_id)
    elif message.reply_to_message and message.chat.id == -880322702:
        chat_id = message.chat.id
        reply_chat_id = message.reply_to_message.forward_from.chat.id
        message_id = message.reply_to_message.message_id
        bot.forward_message(reply_chat_id, chat_id, message_id)
