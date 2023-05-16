from loader import bot
from database import video


@bot.message_handler(content_types=["video"])
def video_s(message):
    if message.video.file_id:
        if not video.find_v(message.video.file_id):
            bot.send_message(message.chat.id, "Видео отправлено на проверку")
            vid = message.video.file_id
            video.add_video(message.from_user.id, vid)
        else:
            bot.send_message(message.chat.id, "Это видео уже отправляли")
