from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from helpers import wrap
from strings import _
from config import BANNED_USERS


@Client.on_message(filters.command("song", "/"))
@wrap
def mistake(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if player.is_currently_playing():
        message.reply_text(
            _("song_1").format(
                '<a href="{}">{}</a>'.format(
                    player.currently_playing["url"], player.currently_playing["title"]
                ),
                player.currently_playing["duration"],
            )
        )
    else:
        message.reply_text(_("song_2"))
