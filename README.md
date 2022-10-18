# Amazon Offers Telegram Bot

<img src="https://user-images.githubusercontent.com/33979978/109801185-70e74580-7c1e-11eb-847a-dbd6e09c21a3.png" alt="logo" width=300>

This project is a Telegram Bot connected to a Telegram Channel that check Amazon offers and send them to your Channel.

## Requirements

### SCRIPT INSTALLER

Now you can run the ```script.sh``` file from the terminal to install all dependencies, included paapi5 package. Open a terminal in the working directory, then type ```bash script.sh``` and launch the command. 



### MANUAL INSTALLER

### **If you used the ```script.sh``` method you can skip the following step.**

In order to use this bot you must complete the following steps:

- Create a telegram bot (https://core.telegram.org/bots)
- Create an Amazon Affiliation (https://programma-affiliazione.amazon.it/)
- Put all of your keys (Amazon and Telegram API Keys) in the code, we are going to define how below

- **Install packages**:
In the root of the project run:
```bash
pip3 install -r requirements.txt
cd paapi5-python-sdk
python3 setup.py build
python3 setup.py install
cd ..
```


## Project Structure

The project is organized like follow:

- **bot.py**
  - Contains the bot start code 

- **consts.py**
  - **HERE YOU MUST PUT YOUR TELEGRAM API KEYS AND PARAMETERS AND YOUR AMAZON API KEYS AND PARAMETERS**
  - **THE CHANNEL_NAME SHOULD START WITH @ (for example @MyChannelName)**
  

- **amazon_api.py**
  - Contain amazon api function to search products


- **response_parser.py**
  - Util functions that parse amazon api response


- **create_messages**
  - message creation functions

## How it works
The bot is running in a while loop, you can define your favorite parameters for:
- Hours of activity
- Pause time between messages
- Amazon Search Categories
- Search Keywords



The bot is active if the time is between **MIN_HOUR** and **MAX_HOUR** (_you can deactivate it during the night for example_)  , you can define these parameters in the code.

The do a break for defined **PAUSE_MINUTE** after sent a message.

You can also edit message body in ```create_messages.py```.

The bot make all http requests to Amazon API at start, save a list of all results in RAM and as long as there are items in results list it:
1. SEND OFFER MESSAGE
2. PAUSE FOR PAUSE_MINUTES
3. SEND ANOTHER MESSAGE

for all the activity time. When all results have been sent, it restart his loop.

### **NOW YOU CAN SEARCH OVER MULTIPLE CATEGORIES** : _in `bot.py` you need to specify your categories and a list of keywords for each category. The corresponding variable is `categories`, it accept a dictionary like:_ 
```python
{
  "1_CATEGORY_NAME":[LIST OF KEYWORD],
  "2_CATEGORY_NAME":[LIST OF KEYWORD]
}
```
  
## Usage

After cloning the repository, define all parameters in the code, install all packages and then start bot with command:
```python bot.py``` or ```python3 bot.py```
  
## Support 
If you need support for the installation and usage of the library you can write to:
- tgofferbot@gmail.com
  
In order to mantain and improve the library consider to contribute:
  
[![paypal](https://user-images.githubusercontent.com/33979978/187162516-5a6576a0-b44d-4e01-bcc6-fd0c262e683a.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7HWMJSGMCCTB6)

## Message Structure

![image](https://user-images.githubusercontent.com/33979978/109800731-dbe44c80-7c1d-11eb-8316-fd5275cb5b46.png)

This is a generated telegram channel message example, you can edit the message structure on  ```create_messages.py``` code.

## Author

Samir Salman
