import logging
import os
import sys
import re
import requests

from pyrogram import Client, errors, filters
from religram.config import Config

isDevelopment = bool(Config.IS_DEVELOPMENT)

log = logging.getLogger()

Command = Config.COMMAND
whiteList = Config.WHITELIST_USERS
botToken = Config.BOT_TOKEN
LOAD_PLUGINS = Config.LOAD_PLUGINS
NOLOAD_PLUGINS = Config.NOLOAD_PLUGINS

isCi = bool(os.environ.get("IS_CI_RUNNER", False))

if isDevelopment or isCi:
	LOG_FORMAT = "[%(asctime)s.%(msecs)03d] %(filename)s:%(lineno)s %(levelname)s: %(message)s"
	logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
	log.warning("Debug enabled")
else:
	logging.basicConfig(level=logging.WARNING)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    log.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)


if whiteList:
	filterWhitelist = filters.user(whiteList)
else:
	filterWhitelist = filters.incoming


if botToken:
	app = Client(Config.BOT_SESSION, api_id=Config.api_id, api_hash=Config.api_hash, bot_token=botToken)
else:
	app = Client(Config.BOT_SESSION, api_id=Config.api_id, api_hash=Config.api_hash, app_version=Config.app_version, device_model=Config.device_model, system_version=Config.system_version, lang_code=Config.lang_code, workers=Config.WORKERS, test_mode=Config.IS_TEST_MODE)
