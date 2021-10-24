#!/bin/bash
pip install -r requirements.txt
cd paapi5-python-sdk
python setup.py build
python setup.py install
cd ..
python bot.py