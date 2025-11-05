# 1
# python.exe -m pip install --upgrade pip
# or
# pip install --upgrade pip

# 2
# python.exe -m pip install -r requirements.txt
# or
# pip install -r requirements.txt

import time
import datetime
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("TOKEN")

url = f"https://api.telegram.org/bot{bot_token}/"


def last_update(request):
    response = requests.get(request + 'getUpdates')
    print(response)
    response = response.json()
    print(response)
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        # pythonanywhere
        time.sleep(3)
        update = last_update(url)
        if update_id == update['update_id']:
            message_text = get_message_text(update).lower()

            if message_text == 'hi' or message_text == 'hello' or message_text == 'hey':
                send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')

            elif message_text == 'csc31':
                send_message(get_chat_id(update), 'Python')

            elif message_text == 'python':
                send_message(get_chat_id(update), 'version 3.14')

            elif message_text == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')

            # Новые команды
            elif message_text == 'hallo':
                send_message(get_chat_id(update), 'Hallo! everynyan haw ar u bai?')

            elif message_text == 'showtime':
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                send_message(get_chat_id(update), f'time: {current_time}')

            elif message_text == 'bye':
                farewells = ['bye', 'dinaho', 'pakka']
                send_message(get_chat_id(update), random.choice(farewells))

            else:
                send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')
            update_id += 1


if __name__ == '__main__':
    main()