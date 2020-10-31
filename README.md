# Amazon Offers Telegram Bot

This project is a Telegram Bot connected to a Telegram Channel that check Amazon offers and send them to your Channel.

## Requirements

In order to use this bot you must done following step:

- Create a telegram bot (https://core.telegram.org/bots)
- Create an Amazon Affiliation (https://programma-affiliazione.amazon.it/)
- Put all of your keys (Amazon and Telegram API Keys) in the code, we are going to define how below
- **Install packages, you can install them with pip**:
  - python-telegram-bot
  - itertools
  - datetime


- **Install Amazon paapi5 package**:
  - open your terminal
  - go to <project directory>/paapi5-python-sdk
  - launch the command: ```python setup.py ``` or ```python3 setup.py ``` 	


## Project Structure

The project is organized like follow:

- **bot.py**
  - Contains the bot start code **HERE YOU MUST PUT YOUR TELEGRAM API KEYS AND PARAMETERS**


- **amazon_api.py**
  - Contain amazon api function to search products, **HERE YOU MUST PUT YOUR AMAZON API KEYS AND PARAMETERS**


- **response_parser.py**
  - Util functions that parse amazon api response


- **create_messages**
  - message creation functions

## How it works

The bot is running in a while loop, you can define your favorite parameters for:
- Hours of activity
- Pause time between messages
- Amazon Search Category
- Search Keywords

The bot is active if the time is between **MIN_HOUR** and **MAX_HOUR** (_you can deactivate it during the night for example_)  , you can define these parameters in the code.

The do a break for defined **PAUSE_MINUTE** after sent a message.

You can also edit message body in ```create_messages.py```.

The bot make all http requests to Amazon API at start, save a list of all results in RAM and as long as there are items in results list it:
1. SEND OFFER MESSAGE
2. PAUSE FOR PAUSE_MINUTES
3. SEND ANOTHER MESSAGE

for all the activity time. When all results have been sent, it restart his loop.

## Usage

After cloning the repository, define all parameters in the code, install all packages and then start bot with command:
```python bot.py``` or ```python3 bot.py```

## Author

Samir Salman
