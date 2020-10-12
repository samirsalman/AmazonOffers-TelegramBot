# coding: utf-8

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


import os

from setuptools import find_packages, setup  # noqa: H301

NAME = "paapi5-python-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=NAME,
    version=VERSION,
    description="ProductAdvertisingAPI 5.0 Python SDK",
    author="Amazon Product Advertising API Team",
    url="https://github.com/amzn/paapi5-python-sdk",
    keywords=[
        "ProductAdvertisingAPI",
        "pa-api",
        "paapi",
        "amazon",
        "paapi5",
        "paapi5.0",
        "paapi5-python-sdk",
        "getbrowsenodes",
        "getvariations",
        "getitems",
        "searchitems",
    ],
    install_requires=REQUIRES,
    packages=find_packages(),
    license="Apache License 2.0",
    include_package_data=True,
    long_description=read("README.md"),
)
