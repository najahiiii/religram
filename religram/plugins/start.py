from pyrogram import filters, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist

__MODULE__ = "Start"
__HELP__ = """
This is basic plugin, that just response command:
- /start
"""


@app.on_message(filterWhitelist & filters.command(["start"], Command))
async def start_command(client, message):
	await message.reply("Hello {}.\nType /help to get command list".format(message.from_user.first_name))
