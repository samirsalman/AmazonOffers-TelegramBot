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
This sample code snippet is for ProductAdvertisingAPI 5.0's GetVariations API

For more details, refer:
https://webservices.amazon.com/paapi5/documentation/get-variations.html

"""

from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.get_variations_request import GetVariationsRequest
from paapi5_python_sdk.models.get_variations_resource import GetVariationsResource
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException


def get_variations():

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

    """ Specify ASIN """
    asin = "B07H65KP63"

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetVariationsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-variations.html#resources-parameter """
    get_variations_resources = [
        GetVariationsResource.ITEMINFO_TITLE,
        GetVariationsResource.OFFERS_LISTINGS_PRICE,
        GetVariationsResource.VARIATIONSUMMARY_VARIATIONDIMENSION,
    ]

    """ Forming request """
    try:
        get_variations_request = GetVariationsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            asin=asin,
            resources=get_variations_resources,
        )
    except ValueError as exception:
        print("Error in forming GetVariationsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.get_variations(get_variations_request)

        print("API called Successfully")
        print("Complete Response:", response)

        """ Parse response """
        if response.variations_result is not None:
            print("Printing VariationSummary:")
            if (
                response.variations_result.variation_summary is not None
                and response.variations_result.variation_summary.variation_count
                is not None
            ):
                print(
                    "VariationCount: ",
                    response.variations_result.variation_summary.variation_count,
                )

            print("Printing first item information in VariationsResult:")
            item_0 = response.variations_result.items[0]
            if item_0 is not None:
                if item_0.asin is not None:
                    print("ASIN: ", item_0.asin)
                if item_0.detail_page_url is not None:
                    print("DetailPageURL: ", item_0.detail_page_url)
                if (
                    item_0.item_info is not None
                    and item_0.item_info.title is not None
                    and item_0.item_info.title.display_value is not None
                ):
                    print("Title: ", item_0.item_info.title.display_value)
                if (
                    item_0.offers is not None
                    and item_0.offers.listings is not None
                    and item_0.offers.listings[0].price is not None
                    and item_0.offers.listings[0].price.display_amount is not None
                ):
                    print(
                        "Buying Price: ", item_0.offers.listings[0].price.display_amount
                    )
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


def get_variations_with_http_info():

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

    """ Specify ASIN """
    asin = "B07H65KP63"

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetVariationsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-variations.html#resources-parameter """
    get_variations_resources = [
        GetVariationsResource.ITEMINFO_TITLE,
        GetVariationsResource.OFFERS_LISTINGS_PRICE,
        GetVariationsResource.VARIATIONSUMMARY_VARIATIONDIMENSION,
    ]

    """ Forming request """
    try:
        get_variations_request = GetVariationsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            asin=asin,
            resources=get_variations_resources,
        )
    except ValueError as exception:
        print("Error in forming GetVariationsRequest: ", exception)
        return

    try:
        """ Sending request """
        response_with_http_info = default_api.get_variations_with_http_info(
            get_variations_request
        )

        """ Parse response """
        if response_with_http_info is not None:
            print("API called Successfully")
            print("Complete Response Dump:", response_with_http_info)
            print("HTTP Info:", response_with_http_info[2])

            response = response_with_http_info[0]
            if response.variations_result is not None:
                print("Printing VariationSummary:")
                if (
                    response.variations_result.variation_summary is not None
                    and response.variations_result.variation_summary.variation_count
                    is not None
                ):
                    print(
                        "VariationCount: ",
                        response.variations_result.variation_summary.variation_count,
                    )

                print("Printing first item information in VariationsResult:")
                item_0 = response.variations_result.items[0]
                if item_0 is not None:
                    if item_0.asin is not None:
                        print("ASIN: ", item_0.asin)
                    if item_0.detail_page_url is not None:
                        print("DetailPageURL: ", item_0.detail_page_url)
                    if (
                        item_0.item_info is not None
                        and item_0.item_info.title is not None
                        and item_0.item_info.title.display_value is not None
                    ):
                        print("Title: ", item_0.item_info.title.display_value)
                    if (
                        item_0.offers is not None
                        and item_0.offers.listings is not None
                        and item_0.offers.listings[0].price is not None
                        and item_0.offers.listings[0].price.display_amount is not None
                    ):
                        print(
                            "Buying Price: ",
                            item_0.offers.listings[0].price.display_amount,
                        )
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


def get_variations_async():

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

    """ Specify ASIN """
    asin = "B07H65KP63"

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetVariationsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-variations.html#resources-parameter """
    get_variations_resources = [
        GetVariationsResource.ITEMINFO_TITLE,
        GetVariationsResource.OFFERS_LISTINGS_PRICE,
        GetVariationsResource.VARIATIONSUMMARY_VARIATIONDIMENSION,
    ]

    """ Forming request """
    try:
        get_variations_request = GetVariationsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            asin=asin,
            resources=get_variations_resources,
        )
    except ValueError as exception:
        print("Error in forming GetVariationsRequest: ", exception)
        return

    try:
        """ Sending request """
        thread = default_api.get_variations(get_variations_request, async_req=True)
        response = thread.get()

        """ Parse response """
        print("API called Successfully")
        print("Complete Response:", response)

        if response.variations_result is not None:
            print("Printing VariationSummary:")
            if (
                response.variations_result.variation_summary is not None
                and response.variations_result.variation_summary.variation_count
                is not None
            ):
                print(
                    "VariationCount: ",
                    response.variations_result.variation_summary.variation_count,
                )

            print("Printing first item information in VariationsResult:")
            item_0 = response.variations_result.items[0]
            if item_0 is not None:
                if item_0.asin is not None:
                    print("ASIN: ", item_0.asin)
                if item_0.detail_page_url is not None:
                    print("DetailPageURL: ", item_0.detail_page_url)
                if (
                    item_0.item_info is not None
                    and item_0.item_info.title is not None
                    and item_0.item_info.title.display_value is not None
                ):
                    print("Title: ", item_0.item_info.title.display_value)
                if (
                    item_0.offers is not None
                    and item_0.offers.listings is not None
                    and item_0.offers.listings[0].price is not None
                    and item_0.offers.listings[0].price.display_amount is not None
                ):
                    print(
                        "Buying Price: ", item_0.offers.listings[0].price.display_amount
                    )
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


get_variations()
# get_variations_with_http_info()
# get_variations_async()
