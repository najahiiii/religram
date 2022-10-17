import time
import logging
import importlib
import random
import sys
import traceback
import threading
import asyncio

import pyrogram
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, log, Command, isCi

from religram.plugins import ALL_PLUGINS


BOT_RUNTIME = 0
HELP_COMMANDS = {}


loop = asyncio.get_event_loop()

async def get_runtime():
	return BOT_RUNTIME

async def start_bot():
	await app.start()
	for module in ALL_PLUGINS:
		imported_module = importlib.import_module("religram.plugins." + module)
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			imported_module.__MODULE__ = imported_module.__MODULE__
		if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
			if not imported_module.__MODULE__.lower() in HELP_COMMANDS:
				HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
			else:
				raise Exception("Can't have two modules with the same name! Please change one")
		if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
			HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
	log.info("-----------------------")
	log.info("Plugins loaded: " + str(ALL_PLUGINS))
	log.info("-----------------------")
	log.info("Bot run successfully!")

	if isCi:
		log.info("Test is passed!")
	else:
		await idle()

if __name__ == '__main__':
	BOT_RUNTIME = int(time.time())
	loop.run_until_complete(start_bot())
