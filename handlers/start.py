from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helpers import wrap
from strings import _
from config import BANNED_USERS


@Client.on_message(
    filters.command("start", "/") & filters.private
)
@wrap
def start(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    message.reply_text(
        _("start_1"),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                _("start_2"), switch_inline_query_current_chat="")]]
        )
    )


__help__ = {
    "start": [_("help_start"), False]
}
