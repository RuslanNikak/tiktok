import handlers

from loader import bot
from config_data import config
from utils.set_bot_commands import set_default_commands

import flask
import telebot
import requests

from flask import Flask
from pyngrok import ngrok


app = Flask(__name__)

@app.route('/handle_telegram_update', methods=['POST'])
def handle_telegram_update():
    if flask.request.method == "POST":
        json_update = flask.request.get_json()
        update = telebot.types.Update.de_json(json_update)
        bot.process_new_updates([update])
        return "", 200
    return "Hello from Flask!", 200


if __name__ == "__main__":
    bot.delete_webhook()
    set_default_commands(bot)
    url = ngrok.connect(bind_tls=True).public_url

    requests.post(f'https://api.telegram.org/bot{config.BOT_TOKEN}/setWebhook',
                  json={'url': f'{url}/handle_telegram_update'})

    app.run(host="0.0.0.0", port=80)
