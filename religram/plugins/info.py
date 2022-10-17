import os

from pyrogram import filters, errors
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist

__MODULE__ = "Info"
__HELP__ = """
Get your telegram info profile, by using command /info.
For get user id only, use command /id
"""

@app.on_message(filterWhitelist & filters.command(["id"], Command))
async def get_id_command(client, message):
	await message.reply("Your ID: `{}`".format(message.from_user.id))


@app.on_message(filterWhitelist & filters.command(["info"], Command))
async def info_command(client, message):
	user = await client.get_chat(message.from_user.id)
	await client.download_media(user.photo.big_file_id, "religram/cache/{}.png".format(message.from_user.id))

	replyText = "**Info**\n"
	replyText += "ID: {}\n".format(message.from_user.id)
	replyText += "First Name: {}\n".format(message.from_user.first_name)
	replyText += "Last Name: {}\n".format(message.from_user.last_name)
	replyText += "Username: {}\n".format(message.from_user.username)
	await message.reply_photo("religram/cache/{}.png".format(message.from_user.id), caption=replyText)

	os.remove("religram/cache/{}.png".format(message.from_user.id))