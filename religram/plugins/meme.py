import random

from pyrogram import filters, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from religram import app, Command, filterWhitelist

__MODULE__ = "Meme"
__HELP__ = """
Reply someone message with /curse command, bot will reply to that message with cursed word
"""

@app.on_message(filterWhitelist & filters.command(["curse"], Command))
async def curse_command(client, message):
	if message.reply_to_message and message.reply_to_message.id:
		text = message.reply_to_message.text
		emojis = ["😂", "😂", "👌", "✌️", "💞", "👍", "👌", "💯", "🎶", "👀", "😂", "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩", "😏", "👉👌", "👀", "👅", "😩", "🚰"]
		reply_text = random.choice(emojis)
		b_char = random.choice(text).lower()
		for c in text:
			if c == " ":
				reply_text += random.choice(emojis)
			elif c in emojis:
				reply_text += c
				reply_text += random.choice(emojis)
			elif c.lower() == b_char:
				reply_text += "🅱️"
			else:
				if bool(random.getrandbits(1)):
					reply_text += c.upper()
				else:
					reply_text += c.lower()
		reply_text += random.choice(emojis)
		await message.reply(reply_text, reply_to_message_id=message.reply_to_message.id)