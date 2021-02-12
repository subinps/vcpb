import subprocess
from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUDO_FILTER, BANNED_USERS
from strings import _


@Client.on_callback_query(filters.regex(".+volume"))
def callback(client, query):
    if query.from_user.id in BANNED_USERS:
        query.reply_text(_("ban_9"))
        return
    if query.from_user.id not in SUDO_FILTER:
        query.reply_text(_("n4u"))
        return
    current_volume = int(query.message.text.split()[-1].replace("%", ""))

    if query.data == "decrease_volume":
        volume = current_volume - 1

        if volume < 0:
            volume = 0

        volume = f"{volume}%"

        subprocess.Popen(["pactl", "set-sink-volume", "MySink", volume]).wait()

        query.message.reply_text(
            _("volume_1").format(volume),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➖", callback_data="decrease_volume"),
                        InlineKeyboardButton("➕", callback_data="increase_volume"),
                    ]
                ]
            ),
            quote=False,
        )
        query.message.delete()
        query.answer()
    elif query.data == "increase_volume":
        volume = current_volume + 1

        if volume > 100:
            volume = 100

        volume = f"{volume}%"

        subprocess.Popen(["pactl", "set-sink-volume", "MySink", volume]).wait()

        query.message.reply_text(
            _("volume_1").format(volume),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➖", callback_data="decrease_volume"),
                        InlineKeyboardButton("➕", callback_data="increase_volume"),
                    ]
                ]
            ),
            quote=False,
        )
        query.message.delete()
        query.answer()

