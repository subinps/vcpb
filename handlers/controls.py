
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from helpers import wrap, State
from config import SUDO_FILTER, BANNED_USERS
from strings import _


@Client.on_message(
    filters.command("pause", "/")
)
@wrap
def pause(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if not player.mpv.pause:
        player.mpv.pause = True
        message.reply_text(_("pause_1"))
    else:
        message.reply_text(_("pause_2"))


@Client.on_message(
    (
        filters.command("resume", "/")
        | filters.command("play", "/")
    )
)
@wrap
def resume(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if player.mpv.pause:
        player.mpv.pause = False
        message.reply_text(_("pause_3"))
    else:
        message.reply_text(_("pause_4"))


@Client.on_message(
    filters.command("skip", "/")
)
@wrap
def skip(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if player.mpv.filename:
        player.mpv.stop()
        message.reply_text(_("skip_1"))
    else:
        message.reply_text(_("skip_2"))


@Client.on_message(
    filters.command("seekf", "/")
)
def seekf(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if player.mpv.filename or player.mpv.pause:
        try:
            player.mpv.seek(int(message.command[1]))
            message.reply_text(_("seek_1"))
        except:
            message.reply_text(_("seek_2"))
    else:
        message.reply_text(_("seek_3"))


@Client.on_message(
    filters.command("seekb", "/")
)
def seekb(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if player.mpv.filename or player.mpv.pause:
        try:
            player.mpv.seek(-int(message.command[1]))
            message.reply_text(_("seek_1"))
        except:
            message.reply_text(_("seek_2"))
    else:
        message.reply_text(_("seek_3"))


__help__ = {
    "pause": [_("help_pause"), True],
    "resume": [_("help_resume"), True],
    "play": [_("help_play"), True],
    "skip": [_("help_skip"), True],
    "seekf": [_("help_seekf"), True],
    "seekb": [_("help_seekb"), True],
}
