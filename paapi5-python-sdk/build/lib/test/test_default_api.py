# -*- coding: utf-8 -*-

# flake8: noqa

from __future__ import absolute_import

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

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""

import unittest

import simplejson as json

from paapi5_python_sdk import (
    GetBrowseNodesRequest,
    GetItemsRequest,
    GetVariationsRequest,
    SearchItemsRequest,
)
from paapi5_python_sdk.api.default_api import DefaultApi  # noqa: E501
from paapi5_python_sdk.api_client import ApiClient
from paapi5_python_sdk.configuration import Configuration
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException


INCOMPLETE_SIGNATURE = "IncompleteSignature"
UNRECOGNIZED_CLIENT = "UnrecognizedClient"
DUMMY_ACCESS_KEY = "DUMMY ACCESS KEY"
DUMMY_SECRET_KEY = "DUMMY SECRET KEY"


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def test_get_browse_nodes_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            response = default_api.get_browse_nodes(get_browse_node_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            response = default_api.get_browse_nodes(get_browse_node_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_http_Info_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            response = default_api.get_browse_nodes_with_http_info(
                get_browse_node_request
            )
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_http_Info_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            response = default_api.get_browse_nodes_with_http_info(
                get_browse_node_request
            )
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            thread = default_api.get_browse_nodes(
                get_browse_node_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            thread = default_api.get_browse_nodes(
                get_browse_node_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_http_Info_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            thread = default_api.get_browse_nodes_with_http_info(
                get_browse_node_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_browse_nodes_http_info_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            browse_node_ids=[],
            resources=[],
        )

        try:
            thread = default_api.get_browse_nodes_with_http_info(
                get_browse_node_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    #############################################################

    def test_get_items_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            response = default_api.get_items(get_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_items_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            response = default_api.get_items(get_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_items_http_Info_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            response = default_api.get_items_with_http_info(get_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_items_http_Info_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            response = default_api.get_items_with_http_info(get_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_items_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            thread = default_api.get_items(get_items_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_items_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            thread = default_api.get_items(get_items_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_items_http_Info_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            thread = default_api.get_items_with_http_info(
                get_items_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_items_http_info_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_items_request = GetItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            item_ids=[],
            resources=[],
        )
        try:
            thread = default_api.get_items_with_http_info(
                get_items_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    #############################################################

    def test_get_variations_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            response = default_api.get_variations(get_variations_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_variations_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            response = default_api.get_variations(get_variations_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_variations_http_Info_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            response = default_api.get_variations_with_http_info(get_variations_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_variations_http_Info_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            response = default_api.get_variations_with_http_info(get_variations_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_variations_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            thread = default_api.get_variations(get_variations_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_variations_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            thread = default_api.get_variations(get_variations_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_get_variations_http_Info_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            thread = default_api.get_variations_with_http_info(
                get_variations_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_get_variations_http_info_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        get_variations_request = GetVariationsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            asin="",
            resources=[],
        )
        try:
            thread = default_api.get_variations_with_http_info(
                get_variations_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    #############################################################

    def test_search_items_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            response = default_api.search_items(search_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_search_items_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            response = default_api.search_items(search_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_search_items_http_Info_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            response = default_api.search_items_with_http_info(search_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_search_items_http_Info_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        default_api = DefaultApi(access_key="", secret_key="", host=host, region=region)

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            response = default_api.search_items_with_http_info(search_items_request)
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_search_items_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            thread = default_api.search_items(search_items_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_search_items_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            thread = default_api.search_items(search_items_request, async_req=True)
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass

    def test_search_items_http_Info_aync_IncompleteSignature(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key=DUMMY_ACCESS_KEY,
            secret_key=DUMMY_SECRET_KEY,
            host=host,
            region=region,
            api_client=api_client,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            thread = default_api.search_items_with_http_info(
                search_items_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 400, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                INCOMPLETE_SIGNATURE,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The request signature did not include all of the required components. If you are using an AWS SDK, requests are signed for you automatically; otherwise, go to https://webservices.amazon.com/paapi5/documentation/sending-request.html#signing.",
                "Message Check",
            )

    pass

    def test_search_items_http_info_aync_UnrecognizedClient(self):
        host = "webservices.amazon.com"
        region = "us-east-1"
        connetion_pool_max_size = 12
        configuration = Configuration()
        configuration.__init__(connetion_pool_max_size)
        api_client = ApiClient(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            configuration=configuration,
        )
        default_api = DefaultApi(
            access_key="",
            secret_key="",
            host=host,
            region=region,
            api_client=api_client,
        )

        search_items_request = SearchItemsRequest(
            partner_tag="",
            partner_type=PartnerType.ASSOCIATES,
            keywords="",
            search_index="All",
            resources=[],
        )
        try:
            thread = default_api.search_items_with_http_info(
                search_items_request, async_req=True
            )
            api_client.__del__()
            response = thread.get()
        except ApiException as exception:
            self.assertEquals(exception.status, 401, "Status Check")
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Code"],
                UNRECOGNIZED_CLIENT,
                "Error Code Check",
            )
            self.assertEquals(
                (json.loads(exception.body)["Errors"])[0]["Message"],
                "The Access Key ID or security token included in the request is invalid.",
                "Message Check",
            )

    pass


if __name__ == "__main__":
    unittest.main()
