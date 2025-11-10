import time
import datetime
import requests
import random
from calculator import calculate_exspression

bot_key = '6798749998:AAHJmEGyF_8jH-WU1r1uNXoVOn-I18WQOeQ'
url = f"https://api.telegram.org/bot{bot_key}/"


def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    r = requests.get(url + "getUpdates", params=params)
    return r.json()

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_message(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    return requests.post(url + "sendMessage", data=params)



def main():
    offset = None

    while True:
        updates = get_updates(offset)

        if "result" in updates:
            for upd in updates["result"]:
                # Сразу готовим offset, чтобы НИКОГДА снова не получить это сообщение
                offset = upd["update_id"] + 1

                if "message" not in upd:
                    continue

                chat_id = upd["message"]["chat"]["id"]
                text = upd["message"].get("text", "").lower()

                # === ТВОИ КОМАНДЫ ===
                if text in ("hai", "hallo", "oi"):
                    send_message(chat_id, "Hallo! everynyan haw ar u? bai")

                elif text == "showtime":
                    t = datetime.datetime.now().strftime("%H:%M:%S")
                    send_message(chat_id, f"time: {t}")

                elif text == "python":
                    send_message(chat_id, "version 3.14")

                elif text == "dice":
                    d1, d2 = random.randint(1, 6), random.randint(1, 6)
                    send_message(chat_id, f"You have {d1} and {d2}! Result = {d1 + d2}")

                elif text == "bai":
                    send_message(chat_id, random.choice(["bye", "dinaho", "pakka"]))

                else:
                    result = calculate_exspression(send_message(get_updates))
                    if result is not None:
                        send_message(get_chat_id(get_updates), result)
                    else:
                        send_message(chat_id, "Sorry, I don't understand you :(")

        time.sleep(0.5)



if __name__ == "__main__":
    main()
