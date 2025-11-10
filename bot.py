import time
import datetime
import requests
import random
from calculator import calculate_exspression

bot_key = '6798749998:AAHJmEGyF_8jH-WU1r1uNXoVOn-I18WQOeQ'

url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!


def last_update(request):
    response = requests.get(request + 'getUpdates')

    # print(response)
    response = response.json()
    # print(response)
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
    try:
        update_id = last_update(url)['update_id']
        while True:
            # pythonanywhere
            time.sleep(3)
            update = last_update(url)
            if update_id == update['update_id']:
                if get_message_text(update).lower() == 'hai' or get_message_text(
                        update).lower() == 'hallo' or get_message_text(update).lower() == 'oi':
                    send_message(get_chat_id(update), 'Hallo! everynyan haw ar u bai?')
                elif get_message_text(update).lower() == 'showtime':
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    send_message(get_chat_id(update), f'time: {current_time}')
                elif get_message_text(update).lower() == 'bai':
                    send_message(get_chat_id(update), 'Finish')
                    break
                elif get_message_text(update).lower() == 'python':
                    send_message(get_chat_id(update), 'version 3.10')
                elif get_message_text(update).lower() == 'dice':
                    _1 = random.randint(1, 6)
                    _2 = random.randint(1, 6)
                    send_message(get_chat_id(update),
                                 'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
                else:
                    result = calculate_exspression(get_message_text(update))
                    if result is not None:
                        send_message(get_chat_id(update), result)
                    else:
                        send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')

                update_id += 1
    except KeyboardInterrupt:
        print('\nБот зупинено')


# print(__name__)
if __name__ == '__main__':
    main()
# print(__name__)
# print('HELLO') #При подключении файла как бибилиотеки import bot, в другой .py файл проекта, этот код будет запускатся при включении того, другого файла