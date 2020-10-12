# -*- coding: utf-8 -*-

"""
 Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License").
 You may not use this file except in compliance with the License.
 A copy of the License is located at

     http://www.apache.org/licenses/LICENSE-2.0

 or in the "license" file accompanying this file. This file is distributed
 on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied. See the License for the specific language governing
 permissions and limitations under the License.
"""

"""
 ProductAdvertisingAPI
 
 https://webservices.amazon.com/paapi5/documentation/index.html
 
"""

"""
This sample code snippet is for ProductAdvertisingAPI 5.0's GetItems API

For more details, refer:
https://webservices.amazon.com/paapi5/documentation/get-items.html

"""

from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.condition import Condition
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException


def parse_response(item_response_list):
    """
    The function parses GetItemsResponse and creates a dict of ASIN to Item object
    :param item_response_list: List of Items in GetItemsResponse
    :return: Dict of ASIN to Item object
    """
    mapped_response = {}
    for item in item_response_list:
        mapped_response[item.asin] = item
    return mapped_response


def get_items():
    """ Following are your credentials """
    """ Please add your access key here """
    access_key = "<YOUR ACCESS KEY>"

    """ Please add your secret key here """
    secret_key = "<YOUR SECRET KEY>"

    """ Please add your partner tag (store/tracking id) here """
    partner_tag = "<YOUR PARTNER TAG>"

    """ PAAPI host and region to which you want to send request """
    """ For more details refer: https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region"""
    host = "webservices.amazon.com"
    region = "us-east-1"

    """ API declaration """
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    """ Request initialization"""

    """ Choose item id(s) """
    item_ids = ["059035342X", "B00X4WHP5E", "B00ZV9RDKK"]

    """ Choose resources you want from GetItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-items.html#resources-parameter """
    get_items_resource = [
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    """ Forming request """

    try:
        get_items_request = GetItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            condition=Condition.NEW,
            item_ids=item_ids,
            resources=get_items_resource,
        )
    except ValueError as exception:
        print("Error in forming GetItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.get_items(get_items_request)

        print("API called Successfully")
        print("Complete Response:", response)

        """ Parse response """
        if response.items_result is not None:
            print("Printing all item information in ItemsResult:")
            response_list = parse_response(response.items_result.items)
            for item_id in item_ids:
                print("Printing information about the item_id: ", item_id)
                if item_id in response_list:
                    item = response_list[item_id]
                    if item is not None:
                        if item.asin is not None:
                            print("ASIN: ", item.asin)
                        if item.detail_page_url is not None:
                            print("DetailPageURL: ", item.detail_page_url)
                        if (
                            item.item_info is not None
                            and item.item_info.title is not None
                            and item.item_info.title.display_value is not None
                        ):
                            print("Title: ", item.item_info.title.display_value)
                        if (
                            item.offers is not None
                            and item.offers.listings is not None
                            and item.offers.listings[0].price is not None
                            and item.offers.listings[0].price.display_amount is not None
                        ):
                            print(
                                "Buying Price: ",
                                item.offers.listings[0].price.display_amount,
                            )
                else:
                    print("Item not found, check errors")

        if response.errors is not None:
            print("\nPrinting Errors:\nPrinting First Error Object from list of Errors")
            print("Error code", response.errors[0].code)
            print("Error message", response.errors[0].message)

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


def get_items_with_http_info():
    """ Following are your credentials """
    """ Please add your access key here """
    access_key = "<YOUR ACCESS KEY>"

    """ Please add your secret key here """
    secret_key = "<YOUR SECRET KEY>"

    """ Please add your partner tag (store/tracking id) here """
    partner_tag = "<YOUR PARTNER TAG>"

    """ PAAPI host and region to which you want to send request """
    """ For more details refer: https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region"""
    host = "webservices.amazon.com"
    region = "us-east-1"

    """ API declaration """
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    """ Request initialization"""

    """ Choose item id(s) """
    item_ids = ["059035342X", "B00X4WHP5E", "B00ZV9RDKK"]

    """ Choose resources you want from GetItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-items.html#resources-parameter """
    get_items_resource = [
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    """ Forming request """
    try:
        get_items_request = GetItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            condition=Condition.NEW,
            item_ids=item_ids,
            resources=get_items_resource,
        )
    except ValueError as exception:
        print("Error in forming GetItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response_with_http_info = default_api.get_items_with_http_info(
            get_items_request
        )

        """ Parse response """
        if response_with_http_info is not None:
            print("API called Successfully")
            print("Complete Response Dump:", response_with_http_info)
            print("HTTP Info:", response_with_http_info[2])

            response = response_with_http_info[0]
            if response.items_result is not None:
                print("Printing all item information in ItemsResult:")
                response_list = parse_response(response.items_result.items)
                for item_id in item_ids:
                    print("Printing information about the item_id: ", item_id)
                    if item_id in response_list:
                        item = response_list[item_id]
                        if item is not None:
                            if item.asin is not None:
                                print("ASIN: ", item.asin)
                            if item.detail_page_url is not None:
                                print("DetailPageURL: ", item.detail_page_url)
                            if (
                                item.item_info is not None
                                and item.item_info.title is not None
                                and item.item_info.title.display_value is not None
                            ):
                                print("Title: ", item.item_info.title.display_value)
                            if (
                                item.offers is not None
                                and item.offers.listings is not None
                                and item.offers.listings[0].price is not None
                                and item.offers.listings[0].price.display_amount
                                is not None
                            ):
                                print(
                                    "Buying Price: ",
                                    item.offers.listings[0].price.display_amount,
                                )
                    else:
                        print("Item not found, check errors")

            if response.errors is not None:
                print(
                    "\nPrinting Errors:\nPrinting First Error Object from list of Errors"
                )
                print("Error code", response.errors[0].code)
                print("Error message", response.errors[0].message)

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


def get_items_async():
    """ Following are your credentials """
    """ Please add your access key here """
    access_key = "<YOUR ACCESS KEY>"

    """ Please add your secret key here """
    secret_key = "<YOUR SECRET KEY>"

    """ Please add your partner tag (store/tracking id) here """
    partner_tag = "<YOUR PARTNER TAG>"

    """ PAAPI host and region to which you want to send request """
    """ For more details refer: https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region"""
    host = "webservices.amazon.com"
    region = "us-east-1"

    """ API declaration """
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    """ Request initialization"""

    """ Choose item id(s) """
    item_ids = ["059035342X", "B00X4WHP5E", "B00ZV9RDKK"]

    """ Choose resources you want from GetItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-items.html#resources-parameter """
    get_items_resource = [
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    """ Forming request """
    try:
        get_items_request = GetItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            condition=Condition.NEW,
            item_ids=item_ids,
            resources=get_items_resource,
        )
    except ValueError as exception:
        print("Error in forming GetItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        thread = default_api.get_items(get_items_request, async_req=True)
        response = thread.get()

        print("API called Successfully")
        print("Complete Response:", response)

        """ Parse response """
        if response.items_result is not None:
            print("Printing all item information in ItemsResult:")
            response_list = parse_response(response.items_result.items)
            for item_id in item_ids:
                print("Printing information about the item_id: ", item_id)
                if item_id in response_list:
                    item = response_list[item_id]
                    if item is not None:
                        if item.asin is not None:
                            print("ASIN: ", item.asin)
                        if item.detail_page_url is not None:
                            print("DetailPageURL: ", item.detail_page_url)
                        if (
                            item.item_info is not None
                            and item.item_info.title is not None
                            and item.item_info.title.display_value is not None
                        ):
                            print("Title: ", item.item_info.title.display_value)
                        if (
                            item.offers is not None
                            and item.offers.listings is not None
                            and item.offers.listings[0].price is not None
                            and item.offers.listings[0].price.display_amount is not None
                        ):
                            print(
                                "Buying Price: ",
                                item.offers.listings[0].price.display_amount,
                            )
                else:
                    print("Item not found, check errors")

        if response.errors is not None:
            print("\nPrinting Errors:\nPrinting First Error Object from list of Errors")
            print("Error code", response.errors[0].code)
            print("Error message", response.errors[0].message)

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


get_items()
# get_items_with_http_info()
# get_items_async()
