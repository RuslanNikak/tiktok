from loader import bot
from keyboards.inline import check_video
from states.users_states import MyStates

from telebot import custom_filters


@bot.message_handler(state=MyStates.bot, chat_id=[-880322702,], is_reply=True,)
def reply_m(message):
    bot.edit_message_caption(
        message.text,
        message.chat.id,
        message.reply_to_message.message_id,
        reply_markup=check_video.keyboard(),
    )


bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(custom_filters.ChatFilter())
