import re

from pyrogram import filters, errors, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist
from religram.helpers.misc import paginate_modules
from __main__ import HELP_COMMANDS

HELP_STRINGS = f"""
Hello there!

__**Check command bellow to see my features!**__
"""

async def help_parser(client, chat_id, text, keyboard=None):
	if not keyboard:
		keyboard = InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help"))
	await client.send_message(chat_id, text, reply_markup=keyboard)


@app.on_message(filterWhitelist & filters.command(["help"]))
async def help_command(client, message):
	if message.chat.type != enums.ChatType.PRIVATE:
		myusername = (await app.get_me()).username
		keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", url=f"t.me/{myusername}?start=help")]])
		await message.reply("You can contact me in private for command list.", reply_markup=keyboard)
		return
	await help_parser(client, message.chat.id, HELP_STRINGS)


def help_button_callback(flt, _, query):
	if re.match(r"help_", query.data):
		return True

help_button_create = filters.create(help_button_callback)

@app.on_callback_query(filterWhitelist & help_button_create)
async def help_button(client, query):
	mod_match = re.match(r"help_module\((.+?)\)", query.data)
	prev_match = re.match(r"help_prev\((.+?)\)", query.data)
	next_match = re.match(r"help_next\((.+?)\)", query.data)
	back_match = re.match(r"help_back", query.data)
	if True:
		if mod_match:
			module = mod_match.group(1)
			text = "__This is help for the module **{}**__:\n".format(HELP_COMMANDS[module].__MODULE__) \
				   + HELP_COMMANDS[module].__HELP__

			await query.message.edit(text=text,
								  reply_markup=InlineKeyboardMarkup(
										[[InlineKeyboardButton(text="⬅️ Back", callback_data="help_back")]]))

		elif prev_match:
			curr_page = int(prev_match.group(1))
			await query.message.edit_text(text=HELP_STRINGS,
								  reply_markup=InlineKeyboardMarkup(
										paginate_modules(curr_page - 1, HELP_COMMANDS, "help")))

		elif next_match:
			next_page = int(next_match.group(1))
			await query.message.edit(text=HELP_STRINGS,
								  reply_markup=InlineKeyboardMarkup(
										paginate_modules(next_page + 1, HELP_COMMANDS, "help")))

		elif back_match:
			await query.message.edit(text=HELP_STRINGS,
								  reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")))

		return await client.answer_callback_query(query.id)

