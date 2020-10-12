import telegram
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
from paapi5_python_sdk.rest import ApiException
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time



TOKEN = '1335257776:AAGVntrtlXJ9ADDEoBdLMHrfjl5bWHRYEXI'

#instanciate the bot
bot = telegram.Bot(token=TOKEN)

#to send message in channel
#status = bot.send_message(chat_id="@RisparmiHandy", text="Test", parse_mode=telegram.ParseMode.HTML)



def parse_response(response):
    items = response.search_result.items
    res_items = []

    for item_0 in items:
        it_parsed = {}



        if item_0 is not None:

            if item_0.images.primary.large is not None:
                it_parsed["image"] = item_0.images.primary.large.url

            if item_0.item_info.features is not None and item_0.item_info.features.display_values is not None:
                desc = ""
                tmp = item_0.item_info.features.display_values
                length = 0
                for el in tmp:
                    if length < 3:
                        desc += el
                        length += 1
                    else:
                        break
                if len(desc)>24:
                    it_parsed["description"] = desc[0:24]

            if item_0.offers is not None and item_0.offers.listings[0] is not None and item_0.offers.listings[0].price.savings is not None:
                if item_0.offers.listings[0].is_buy_box_winner is not None:
                    it_parsed["off"] = item_0.offers.listings[0].is_buy_box_winner


                it_parsed["savings"] = item_0.offers.listings[0].price.savings.amount
                op = float(item_0.offers.listings[0].price.savings.amount) + float(item_0.offers.listings[0].price.amount)
                it_parsed["original_price"] = '%.2f'%(op)



            if item_0.asin is not None:
                it_parsed["id"] = item_0.asin
            if item_0.detail_page_url is not None:
                it_parsed["url"] = item_0.detail_page_url
            if (
                    item_0.item_info is not None
                    and item_0.item_info.title is not None
                    and item_0.item_info.title.display_value is not None
            ):
                it_parsed["title"] = item_0.item_info.title.display_value
            if (
                    item_0.offers is not None
                    and item_0.offers.listings is not None
                    and item_0.offers.listings[0].price is not None
                    and item_0.offers.listings[0].price.display_amount is not None
            ):

                it_parsed["price"] = '{}'.format(item_0.offers.listings[0].price.display_amount).encode('utf-8')
        res_items.append(it_parsed)
    return res_items



#function that search amazon products
def search_items(keywords, search_index="All", item_page=1):

    access_key = "AKIAILT2XQ443ZGHJ35A"

    secret_key = "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"

    partner_tag = "cgm-21"

    host = "webservices.amazon.it"
    region = "eu-west-1"

    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )


    """ Specify the category in which search request is to be made """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/use-cases/organization-of-items-on-amazon/search-index.html """


    """ Specify item count to be returned in search result """
    item_count = 20



    """ Choose resources you want from SearchItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/search-items.html#resources-parameter """
    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
        SearchItemsResource.IMAGES_PRIMARY_LARGE,
        SearchItemsResource.OFFERS_LISTINGS_SAVINGBASIS,
        SearchItemsResource.ITEMINFO_FEATURES,
        SearchItemsResource.OFFERS_LISTINGS_PROMOTIONS,
        SearchItemsResource.OFFERS_LISTINGS_CONDITION,
        SearchItemsResource.OFFERS_LISTINGS_ISBUYBOXWINNER
    ]

    """ Forming request """
    try:
        search_items_request = SearchItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keywords,
            search_index=search_index,
            item_count=item_count,
            resources=search_items_resource,
            item_page=item_page
        )
    except ValueError as exception:
        print("Error in forming SearchItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.search_items(search_items_request)
        print("Request received")
        res = parse_response(response)

        if response.errors is not None:
            print("\nPrinting Errors:\nPrinting First Error Object from list of Errors")
            print("Error code", response.errors[0].code)
            print("Error message", response.errors[0].message)
        return res

    except ApiException as exception:
        print("Error calling PA-API 5.0!")
        print("Status code:", exception.status)
        print("Errors :", exception.body)
        print("Request ID:", exception.headers["x-amzn-RequestId"])

    except TypeError as exception:
        print("TypeError :", exception)

    except ValueError as exception:
        print("ValueError :", exception)

    except Exception as exception:
        print("Exception :", exception)

import random

def create_item_html(items):
    response = []
    print(len(items))

    random.shuffle(items)
    for item in items:
        if 'off' in item:
            keyboard = [
                [InlineKeyboardButton("🛒 Acquista ora 🛒", callback_data='buy', url=item["url"])],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            html = ""
            html += "🎁 <b>{}</b> 🎁\n\n".format(item['title']).encode('utf-8')

            if 'description' in list(item.keys()):
                html += "{}\n".format(item['description']).encode('utf-8')

            html += "<a href='{}'>&#8205</a>\n".format(item['image']).encode('utf-8')

            if 'savings' in list(item.keys()):
                html += "❌ Non più: {}€ ❌\n\n".format(item['original_price']).encode('utf-8')

            html += "💰 <b>Al prezzo di: {}</b> 💰\n\n".format(item['price']).encode('utf-8')

            if 'savings' in list(item.keys()):
                html += "✅ <b>Risparmi: {}€</b> ✅\n\n".format(item['savings']).encode('utf-8')

            html += "<b><a href='{}'></a></b>".format(item['url']).encode('utf-8')

            response.append(html)
            response.append(reply_markup)
    return response



keywords = ["Offerte del giorno", "Offerte a tempo", "Migliori offerte", "Imperdibile", "Offerta", "Sotto costo", "Offertissima", "Offerta della settimana", "Prime day"]

random.shuffle(keywords)
from itertools import chain

while True:
    for el in keywords:
        items_full = []
        for i in range(1,10):
            items = search_items(el, "Electronics", item_page=i)
            time.sleep(1)
            items_full.append(items)

        items_full = list(chain(*items_full))
        res = create_item_html(items_full)
        while len(res) > 3:
            try:
                # status = bot.send_message(chat_id="@RisparmiHandy", text=built_item, parse_mode=telegram.ParseMode.HTML)
                bot.send_message(chat_id="@RisparmiHandy", text=res[0], reply_markup=res[1],
                                          parse_mode=telegram.ParseMode.HTML)
                bot.send_message(chat_id="@RisparmiHandy", text=res[2], reply_markup=res[3],
                                          parse_mode=telegram.ParseMode.HTML)
                res.pop(0)
                res.pop(0)
                res.pop(0)
                res.pop(0)

            except Exception as e:
                print(e)
                res.pop(0)
                res.pop(0)
                res.pop(0)
                res.pop(0)
                continue

            time.sleep(60*15)



