import telegram
from amazon_api import search_items
from create_messages import create_item_html
import time
from datetime import datetime
from itertools import chain
import random

# ********** Author: Samir Salman **********

# ***** Telegram TOKEN and parameters Definition *****
TOKEN = '<YOUR TELEGRAM TOKEN>'
CHANNEL_NAME = '<YOUR TELEGRAM CHANNEL NAME>'

# ***** BOT ACTIVITY TIME *****
MIN_HOUR = 9
MAX_HOUR = 24
PAUSE_MINUTES = 12

# ***** SEARCH CATEGORY DEFINITION *****
CATEGORY = "<SEARCH CATEGORY>"

# Create the bot instance
bot = telegram.Bot(token=TOKEN)

# Search keywords definition
keywords = ["Televisori", "Notebook", "Tablet", "Apple", "Samsung", "Smartwatch", "Auricolari Bluetooth", "Fotocamera",
            "Videocamera"]


# run bot function
def run_bot(bot, keywords):
    # shuffling keywords list
    random.shuffle(keywords)

    # start loop
    while True:
        try:
            items_full = []

            # iterate over keywords
            for el in keywords:
                # iterate over pages
                for i in range(1, 10):

                    items = search_items(el, CATEGORY, item_page=i)

                    # api time limit for another http request is 1 second
                    time.sleep(1)

                    items_full.append(items)

            # concatenate all results
            items_full = list(chain(*items_full))
            print(f'{5 * "*"} Requests Completed {5 * "*"}')

            # shuffling results 5 times
            for t in range(5):
                random.shuffle(items_full)

            # creating html message, you can find more information in create_messages.py
            res = create_item_html(items_full)

            # while we have items in our list
            while len(res) > 3:
                now = datetime.now().time()

                # if bot is active

                if MIN_HOUR - 2 < now.hour < MAX_HOUR - 2:
                    try:
                        # Sending two consecutive messages

                        print(f'{5 * "*"} Sending posts to channel {5 * "*"}')

                        bot.send_message(chat_id=CHANNEL_NAME, text=res[0], reply_markup=res[1],
                                         parse_mode=telegram.ParseMode.HTML)

                        bot.send_message(chat_id=CHANNEL_NAME, text=res[2], reply_markup=res[3],
                                         parse_mode=telegram.ParseMode.HTML)
                        for index in range(3):
                            res.pop(0)

                    except Exception as e:
                        print(e)
                        for index in range(3):
                            res.pop(0)
                        continue

                    # Sleep for PAUSE_MINUTES
                    time.sleep(60 * PAUSE_MINUTES)

                else:
                    # if bot is not active
                    print(f'{5 * "*"} Inactive Bot, between  {MIN_HOUR}AM and {MAX_HOUR}PM {5 * "*"}')
                    time.sleep(60 * 5)

        except Exception as e:
            print(e)


# running bot
run_bot(bot, keywords)
