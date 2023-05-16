from loader import bot
from database import video


@bot.callback_query_handler(func=lambda call: call.data == "1")
def callback_inline_first(call):
    message = call.message
    vid = call.message.video.file_id
    if message.caption:
        caption = f"{message.caption}\n\n<a href='https://t.me/RanDomTikTokBot'>ТиК ТоК Аниме🍀</a>"
        bot.send_video(
            -1001489149248,  # -1001489149248
            message.video.file_id,
            caption=caption,
            parse_mode="HTML",
        )
    else:
        caption = "<a href='https://t.me/RanDomTikTokBot'>ТиК ТоК Аниме🍀</a>"
        bot.send_video(
            -1001489149248,  # -1001489149248
            message.video.file_id,
            caption=caption,
            parse_mode="HTML",
        )
    bot.edit_message_reply_markup(
        message.chat.id, message.message_id, reply_markup=None
    )
    vid = message.video.file_id
    video.video_good(vid[-27:])


@bot.callback_query_handler(func=lambda call: call.data == "2")
def callback_inline_second(call):
    message = call.message
    bot.edit_message_reply_markup(
        message.chat.id, message.message_id, reply_markup=None
    )
    vid = message.video.file_id
    video.video_bad(vid[-27:])
