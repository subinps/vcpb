from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from helpers import wrap
from config import SUDO_FILTER, BANNED_USERS
from strings import _


@Client.on_message(filters.command("clearqueue", "/"))
@wrap
def clear_queue(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    try:
        with player.queue.mutex:
            player.queue.queue.clear()
        message.reply_text(_("queue_4"))
    except:
        message.reply_text(_("error"))


@Client.on_message(filters.command("queue", "/"))
@wrap
def queue(client, message):
    if message.from_user.id in BANNED_USERS:
        message.reply_text(_("ban_9"))
        return
    qsize = player.queue.qsize()

    if qsize == 0:
        return

    queue_ = player.queue.queue
    human_queue = _("queue_1").format(qsize) + "\n"
    count = 1

    for item in queue_:
        human_queue += (
            _("queue_2").format(
                count,
                '<a href="{}">{}</a>'.format(
                    item["url"],
                    item["title"],
                ),
                item["duration"],
            )
            + "\n"
        )
        count += 1

    m = message.reply_text("....")

    try:
        m.edit_text(human_queue, disable_web_page_preview=True)
    except:
        m.edit_text(_("error"))


__help__ = {
    "clearqueue": [_("help_clearqueue"), True],
    "queue": [_("help_queue"), False],
}
