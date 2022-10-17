from pyrogram import filters, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist
from religram.helpers.nekobin import nekobin
from religram.helpers.parser import mention_markdown

# This plugin is meant for developer only
# And wont show up in help module

# If whitelist was for anyone, bot will not load this plugin
if filterWhitelist != filters.incoming:

	@app.on_message(filterWhitelist & filters.command(["log"], Command))
	async def logging_command(client, message):
		data = nekobin(str(message), "Telegram Log", "Religram")
		await message.reply(data)

	@app.on_message(filterWhitelist & filters.command(["dc"], Command))
	async def get_dc_command(client, message):
		chat = message.chat
		user = message.from_user
		if message.reply_to_message:
			if message.reply_to_message.forward_from:
				dc_id = message.reply_to_message.from_user.dc_id
				user = mention_markdown(message.reply_to_message.forward_from.id, message.reply_to_message.forward_from.first_name)
			else:
				dc_id = message.reply_to_message.from_user.dc_id
				user = mention_markdown(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)
		else:
			dc_id = message.from_user.dc_id
			user = mention_markdown(message.from_user.id, message.from_user.first_name)
		if dc_id == 1:
			text = "{}'s assigned datacenter is **DC1**, located in **MIA, Miami FL, USA**".format(user)
		elif dc_id == 2:
			text = "{}'s assigned datacenter is **DC2**, located in **AMS, Amsterdam, NL**".format(user)
		elif dc_id == 3:
			text = "{}'s assigned datacenter is **DC3**, located in **MIA, Miami FL, USA**".format(user)
		elif dc_id == 4:
			text = "{}'s assigned datacenter is **DC4**, located in **AMS, Amsterdam, NL**".format(user)
		elif dc_id == 5:
			text = "{}'s assigned datacenter is **DC5**, located in **SIN, Singapore, SG**".format(user)
		else:
			text = "{}'s assigned datacenter is **Unknown**".format(user)
		await message.reply(text)
