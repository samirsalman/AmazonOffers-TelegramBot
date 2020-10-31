# This function parses amazon response
def parse_response(response):
    items = response.search_result.items
    res_items = []

    for item_0 in items:
        it_parsed = {}

        if item_0 is not None:

            # if contains an image
            if item_0.images.primary.large is not None:
                it_parsed["image"] = item_0.images.primary.large.url

            # if contains a description
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
                if len(desc) > 24:
                    it_parsed["description"] = desc[0:24]

            # if contains price and/or offer price
            if item_0.offers is not None and item_0.offers.listings[0] is not None and item_0.offers.listings[
                0].price.savings is not None:
                if item_0.offers.listings[0].is_buy_box_winner is not None:
                    it_parsed["off"] = item_0.offers.listings[0].is_buy_box_winner

                it_parsed["savings"] = item_0.offers.listings[0].price.savings.amount
                op = float(item_0.offers.listings[0].price.savings.amount) + float(
                    item_0.offers.listings[0].price.amount)
                it_parsed["original_price"] = '%.2f' % (op)

            # get item id
            if item_0.asin is not None:
                it_parsed["id"] = item_0.asin

            # get item amazon url
            if item_0.detail_page_url is not None:
                it_parsed["url"] = item_0.detail_page_url

            # get item title
            if (
                    item_0.item_info is not None
                    and item_0.item_info.title is not None
                    and item_0.item_info.title.display_value is not None
            ):
                it_parsed["title"] = item_0.item_info.title.display_value

            # get item price
            if (
                    item_0.offers is not None
                    and item_0.offers.listings is not None
                    and item_0.offers.listings[0].price is not None
                    and item_0.offers.listings[0].price.display_amount is not None
            ):
                it_parsed["price"] = f'{item_0.offers.listings[0].price.display_amount}'

        res_items.append(it_parsed)
    return res_items
