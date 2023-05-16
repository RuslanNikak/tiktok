from loader import bot
from database import users
from config_data import config
from keyboards.reply import button_users


@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.type == "private":
        if not users.find_id(message.chat.id):
            users.add_users(
                message.from_user.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name,
                message.from_user.language_code,
            )
    bot.send_sticker(message.chat.id, config.STICKER)
    bot.send_message(
        message.chat.id,
        f"Добро пожаловать, <b>{message.from_user.first_name}.</b>\n\n"
        "Этот бот создан админом канала @PortaLToAnime\n"
        "Присылая свои видео или ссылку из Tik Tok, вы помогаете админам\n\n"
        "Спасибо что используете нашего бота)",
        parse_mode="HTML",
        reply_markup=button_users.users(),
    )
    bot.delete_state(message.from_user.id, message.chat.id)
