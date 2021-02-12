from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from helpers import wrap
from strings import _
from config import BANNED_USERS


@Client.on_message(
    (filters.all & ~ filters.text) & filters.private
)
@wrap
def mistake(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    message.reply_text(_("mistake"))
