import requests
from html import escape

from pyrogram import filters, errors
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist

__MODULE__ = "Weather"
__HELP__ = """
Get current weather in your city by using `wt` command.
Example: `/wt jakarta`
"""


@app.on_message(filterWhitelist & filters.command(["wt"], Command))
async def weather_command(client, message):
	if len(message.command) <= 1:
		await message.reply("Usage: `wt city`")
		return
	location = message.command[1]
	headers = {'user-agent': 'httpie'}
	result = requests.get(f"https://wttr.in/{location}?mnTC0&lang=en", headers=headers).text

	if "sorry" in result.lower():
		await message.reply(a.text)
		return

	await message.reply(f"<code>{escape(result)}</code>", parse_mode=ParseMode.HTML)
