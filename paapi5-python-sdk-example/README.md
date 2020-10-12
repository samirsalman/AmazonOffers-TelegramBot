# Product Advertising API 5.0 SDK for Python


[![pypi version](http://img.shields.io/pypi/v/paapi5-python-sdk.svg?style=flat)](https://pypi.python.org/pypi/paapi5-python-sdk/)
[![pypi downloads](https://img.shields.io/pypi/dm/paapi5-python-sdk.svg.svg?style=flat)](https://pypi.python.org/pypi/paapi5-python-sdk/)


This repository contains the official Product Advertising API 5.0 Python SDK called **paapi5-python-sdk** that allows you to access the [Product Advertising API](https://webservices.amazon.com/paapi5/documentation/index.html) from your Python app.

## Requirements

Python 2.7 and 3.4+

## Installation & Usage

### pip install

You can directly install it from pip using:

```sh
pip install paapi5-python-sdk
```

Or, you may also install directly from Github

```sh
pip install git+https://github.com/amzn/paapi5-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/amzn/paapi5-python-sdk.git`)

Then import the package:
```python
import paapi5_python_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import paapi5_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

Simple example for [SearchItems](https://webservices.amazon.com/paapi5/documentation/search-items.html) to discover Amazon products with the keyword 'Harry Potter' in Books category:

```python
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource


def search_items():

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

    """ Specify keywords """
    keywords = "Harry Potter"

    """ Specify the category in which search request is to be made """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/use-cases/organization-of-items-on-amazon/search-index.html """
    search_index = "Books"

    """ Specify item count to be returned in search result """
    item_count = 1

    """ Choose resources you want from SearchItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/search-items.html#resources-parameter """
    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
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
        )
    except ValueError as exception:
        print("Error in forming SearchItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.search_items(search_items_request)

        print("API called Successfully")
        print("Complete Response:", response)

        """ Parse response """
        if response.search_result is not None:
            print("Printing first item information in SearchResult:")
            item_0 = response.search_result.items[0]
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
 
search_items()
```

Complete documentation, installation instructions, and examples are available [here](https://webservices.amazon.com/paapi5/documentation/index.html).

## License
This SDK is distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0), see LICENSE.txt and NOTICE.txt for more information.
