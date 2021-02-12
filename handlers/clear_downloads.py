
import os
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from config import SUDO_FILTER, BANNED_USERS
from strings import _


@Client.on_message(
    filters.command("cleardownloads", "/")
)
def clear_downloads(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    try:
        for file in os.listdir("downloads"):
            try:
                os.remove("downloads/" + file)
            except:
                pass

        message.reply_text(_("cleardownloads"))
    except:
        message.reply_text(_("error"))


__handlers__ = [
    [
        MessageHandler(
            clear_downloads,
            filters.command("cleardownloads", "/")
            & SUDO_FILTER
        )
    ]
]
__help__ = {
    "cleardownloads": [_("help_cleardownloads"), True]
}
