import subprocess
import re
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import player
from helpers import wrap
from config import SUDO_FILTER, BANNED_USERS
from strings import _


@Client.on_message(
    filters.command("volume", "/")
)
@wrap
def volume(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if len(message.text.split()) == 2 and message.from_user.id in SUDO_FILTER:
        try:
            volume = int(message.text.split()[1])
            if volume in range(1, 101):
                volume = f"{volume}%"
                subprocess.Popen(
                    [
                        "pactl",
                        "set-sink-volume",
                        "MySink",
                        volume
                    ]
                ).wait()
                message.reply_text(
                    _("volume_2").format(volume)
                )
                return
        except:
            pass

    current_volume = "".join(re.search(r"Volume\:(.+)\n", subprocess.check_output(
        ["pactl", "list", "sinks"]).decode()).group(0).split()).split("/")[1]

    if message.from_user.id in SUDO_FILTER:
        message.reply_text(
            _("volume_1").format(current_volume),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➖",
                            callback_data="decrease_volume"
                        ),
                        InlineKeyboardButton(
                            "➕",
                            callback_data="increase_volume"
                        )
                    ]
                ]
            ),
            quote=True
        )
    else:
        message.reply_text(
            _("volume_1").format(current_volume),
        )


__help__ = {
    "volume": [_("help_volume"), False]
}
