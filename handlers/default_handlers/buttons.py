from loader import bot
from database import video
from keyboards.reply import button_users
from keyboards.inline import check_video
from keyboards.reply import button_adm
from states.users_states import MyStates


def check(video_1):
    capt = "Статус неизвестен"
    if video_1 == 2:
        capt = "Не проверено⏳"
    elif video_1 == 1:
        capt = "Одобренно✅"
    elif video_1 == 0:
        capt = "Отказано❌"
    return capt


@bot.message_handler(content_types=["text"])
def button(message):
    text = [",jn", ">jn", "бот"]
    if message.text == "Моя статистика":
        bot.send_message(
            message.chat.id, "Выберите действие", reply_markup=button_users.statistik()
        )
    elif message.text == "Мои последние 5 видео":
        videos = video.send_video_limit(message.from_user.id)
        for video_1 in videos:
            file_id = video_1[2]
            cap = check(video_1[3])
            bot.send_video(message.chat.id, file_id, caption=f"\n{cap}")
    elif message.text == "Все видео":
        videos = video.send_video(message.from_user.id)
        for video_1 in videos:
            file_id = video_1[2]
            cap = check(video_1[3])
            bot.send_video(message.chat.id, file_id, caption=f"\n{cap}")
    elif message.text == "Информация о всех видео":
        videos = video.send_video(message.from_user.id)
        all = 0
        good = 0
        bad = 0
        no_watch = 0
        for video_1 in videos:
            all += 1
            if video_1[3] == 2:
                no_watch += 1
            elif video_1[3] == 1:
                good += 1
            elif video_1[3] == 0:
                bad += 1
        if all == 0:
            mess = "Вы еще не отправляли видео"
        elif good == 0 and bad == 0:
            mess = "Подождите пока проверят ваши видео"
        elif good <= bad:
            mess = "Присылайте более качественнее видео "
            "или попробуйте выбрать другую тематику аниме"
        elif good > bad:
            mess = "Спасибо что присылаете нам качественный контент)"
        bot.send_message(
            message.chat.id,
            "Вся информация о ваших видео\n\n"
            f"🍀Всего отправлено видео: {all}\n"
            f"✅Одобрено: {good}\n"
            f"❌Отказано: {bad}\n"
            f"⏳Не проверено: {no_watch}\n\n"
            f"{mess}",
        )
    elif message.text == "На главную":
        bot.send_message(
            message.chat.id, "Выберите действие", reply_markup=button_users.users()
        )
        bot.delete_state(message.from_user.id, message.chat.id)
    elif message.text.lower() in text and message.chat.type == "group":
        bot.send_message(
            message.chat.id,
            "Выберите что хотите сделать",
            reply_markup=button_adm.adm(),
        )
    elif message.text == '777' and message.chat.type == "group":
        bot.set_state(message.from_user.id, MyStates.bot, message.chat.id)
        bot.send_message(
            message.chat.id,
            "Можете писать название\nЧтобы выйти нажмите /stop",
        )
    elif message.text == "Не проверенные видео" and message.chat.type == "group":
        vid = video.no_watch()
        for row in vid:
            bot.send_video(-880322702, row[2], reply_markup=check_video.keyboard())
    elif message.text == "Связаться с админами":
        bot.set_state(message.from_user.id, MyStates.user_id, message.chat.id)
        bot.send_message(
            message.chat.id,
            "Напишите чтобы с вами связались\n" "Чтобы выйти нажмите /stop",
        )
