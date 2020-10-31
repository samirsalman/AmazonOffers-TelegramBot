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
This sample code snippet is for ProductAdvertisingAPI 5.0's GetBrowseNodes API

For more details, refer:
https://webservices.amazon.com/paapi5/documentation/getbrowsenodes.html

"""

from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.get_browse_nodes_request import GetBrowseNodesRequest
from paapi5_python_sdk.models.get_browse_nodes_resource import GetBrowseNodesResource
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException


def parse_response(browse_nodes_response_list):
    """
    The function parses Browse Nodes Response and creates a dict of BrowseNodeID to BrowseNode object
    :param browse_nodes_response_list: List of BrowseNodes in GetBrowseNodes response
    :return: Dict of BrowseNodeID to BrowseNode object
    """
    mapped_response = {}
    for browse_node in browse_nodes_response_list:
        mapped_response[browse_node.id] = browse_node
    return mapped_response


def get_browse_nodes():

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

    """ Specify browse_node id(s) """
    browse_node_ids = ["3040", "0", "3045"]

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetBrowseNodesResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/getbrowsenodes.html#resources-parameter """
    get_browse_node_resources = [
        GetBrowseNodesResource.ANCESTOR,
        GetBrowseNodesResource.CHILDREN,
    ]

    """ Forming request """
    try:
        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            browse_node_ids=browse_node_ids,
            resources=get_browse_node_resources,
        )
    except ValueError as exception:
        print("Error in forming GetBrowseNodesRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.get_browse_nodes(get_browse_node_request)

        print("API called Successfully")
        print("Complete Response:\n", response)

        """ Parse response """
        if response.browse_nodes_result is not None:
            print("Printing all browse node information in BrowseNodesResult:")
            response_list = parse_response(response.browse_nodes_result.browse_nodes)
            for browse_node_id in browse_node_ids:
                print(
                    "Printing information about the browse node with Id: ",
                    browse_node_id,
                )
                if browse_node_id in response_list:
                    browse_node = response_list[browse_node_id]
                    if browse_node is not None:
                        if browse_node.id is not None:
                            print("BrowseNodeId: ", browse_node.id)
                        if browse_node.display_name is not None:
                            print("DisplayName: ", browse_node.display_name)
                        if browse_node.context_free_name is not None:
                            print("ContextFreeName: ", browse_node.context_free_name)
                else:
                    print("BrowseNode not found, check errors")

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


def get_browse_nodes_with_http_info():

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

    """ Specify browse_node id(s) """
    browse_node_ids = ["3040", "0", "3045"]

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetBrowseNodesResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/getbrowsenodes.html#resources-parameter """
    get_browse_node_resources = [
        GetBrowseNodesResource.ANCESTOR,
        GetBrowseNodesResource.CHILDREN,
    ]

    """ Forming request """
    try:
        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            browse_node_ids=browse_node_ids,
            resources=get_browse_node_resources,
        )
    except ValueError as exception:
        print("Error in forming GetBrowseNodesRequest: ", exception)
        return

    try:
        """ Sending request """
        response_with_http_info = default_api.get_browse_nodes_with_http_info(
            get_browse_node_request
        )

        """ Parse response """
        if response_with_http_info is not None:
            print("API called Successfully")
            print("Complete Response Dump:", response_with_http_info)
            print("HTTP Info:", response_with_http_info[2])

            response = response_with_http_info[0]
            if response.browse_nodes_result is not None:
                print("Printing all browse node information in BrowseNodesResult:")
                response_list = parse_response(
                    response.browse_nodes_result.browse_nodes
                )
                for browse_node_id in browse_node_ids:
                    print(
                        "Printing information about the browse node with Id: ",
                        browse_node_id,
                    )
                    if browse_node_id in response_list:
                        browse_node = response_list[browse_node_id]
                        if browse_node is not None:
                            if browse_node.id is not None:
                                print("BrowseNodeId: ", browse_node.id)
                            if browse_node.display_name is not None:
                                print("DisplayName: ", browse_node.display_name)
                            if browse_node.context_free_name is not None:
                                print(
                                    "ContextFreeName: ", browse_node.context_free_name
                                )
                    else:
                        print("BrowseNode not found, check errors")

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


def get_browse_nodes_async():

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

    """ Specify browse_node id(s) """
    browse_node_ids = ["3040", "0", "3045"]

    """ Specify language of preference """
    """ For more details, refer https://webservices.amazon.com/paapi5/documentation/locale-reference.html"""
    languages_of_preference = ["es_US"]

    """ Choose resources you want from GetBrowseNodesResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/getbrowsenodes.html#resources-parameter """
    get_browse_node_resources = [
        GetBrowseNodesResource.ANCESTOR,
        GetBrowseNodesResource.CHILDREN,
    ]

    """ Forming request """
    try:
        get_browse_node_request = GetBrowseNodesRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            languages_of_preference=languages_of_preference,
            browse_node_ids=browse_node_ids,
            resources=get_browse_node_resources,
        )
    except ValueError as exception:
        print("Error in forming GetBrowseNodesRequest: ", exception)
        return

    try:
        """ Sending request """
        thread = default_api.get_browse_nodes(get_browse_node_request, async_req=True)
        response = thread.get()

        print("API called Successfully")
        print("Complete Response:", response)

        """ Parse response """
        if response.browse_nodes_result is not None:
            print("Printing all browse node information in BrowseNodesResult:")
            response_list = parse_response(response.browse_nodes_result.browse_nodes)
            for browse_node_id in browse_node_ids:
                print(
                    "Printing information about the browse node with Id: ",
                    browse_node_id,
                )
                if browse_node_id in response_list:
                    browse_node = response_list[browse_node_id]
                    if browse_node is not None:
                        if browse_node.id is not None:
                            print("BrowseNodeId: ", browse_node.id)
                        if browse_node.display_name is not None:
                            print("DisplayName: ", browse_node.display_name)
                        if browse_node.context_free_name is not None:
                            print("ContextFreeName: ", browse_node.context_free_name)
                else:
                    print("BrowseNode not found, check errors")

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


get_browse_nodes()
# get_browse_nodes_with_http_info()
# get_browse_nodes_async()
