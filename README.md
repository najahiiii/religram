# Religram
Religram is userbot of Telegram, yes userbot which using your main account or your dummy account, as a bot

# Installation
- First, you need to have Python and Python-pip at least version 3.6 or newer
- Then, run the installation with: `pip3 install -r requirements.txt`

# Configuration
1. Register your account API [here](https://my.telegram.org/apps)
2. Copy api_id and api_hash for config later.
3. Go to [@EmiliaHikariBot](https://t.me/EmiliaHikariBot) or [@MissRose_bot](https://t.me/MissRose_bot), and type `/id`. Copy your ID account for later.

### Using config file
You can use easily config with config.py file.

1. Rename config.example.py to **confing.py** in religram folder
2. And change config like this:

```
api_id = 12345 # From guide no 2
api_hash = "123456789abcdefghijklmnopqrstuvw" # From guide no 2

BOT_TOKEN = "TOKEN" # Replace TOKEN from guide above (@BotFather)
```

# Running
- To run the bot, do: `python3 -m religram`

# [Contribution](https://github.com/najahiiii/religram/blob/main/CONTRIBUTING.md)
- Fork this repo
- Create your own plugin on `religram/plugins/` by create a new file with `<newplugin>.py` (fill `newplugin` to your desire, recommended to copy paste from `start.py`)
- Make sure your `__MODULE__` has no same to another plugin
- And test it by running your bot
- After all ok, you can [Pull Request](https://github.com/najahiiii/religram/pulls)
