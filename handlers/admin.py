from config import SUDO_FILTER, BANNED_USERS, OWNER
from pyrogram import Client, filters
from strings import _
from helpers import wrap


@Client.on_message(filters.command(["sudo"]))
@wrap
def adduser(client, message):
    if message.from_user.id not in OWNER:
        message.reply_text(_("n4u"))
    else:
        if len(message.text.split(" ")) != 2:
            message.reply_text(_("admin_6"))
            return
        try:
            newadmin = int(message.text.split()[1])
            if newadmin in BANNED_USERS:
                message.reply_text(_("admin_5"))
                return
            if newadmin in SUDO_FILTER:
                message.reply_text(_("admin_3"))
                return
            if newadmin not in SUDO_FILTER:
                SUDO_FILTER.add(newadmin)
                message.reply_text(_("admin_1"))
        except:
            message.reply_text(_("admin_6"))


@Client.on_message(filters.command(["nosudo"]))
@wrap
def removeuser(client, message):
    if message.from_user.id not in OWNER:
        message.reply_text(_("n4u"))
    else:
        if len(message.text.split(" ")) != 2:
            message.reply_text(_("admin_6"))
            return
        try:
            remadmin = int(message.text.split()[1])
            if remadmin not in SUDO_FILTER:
                message.reply_text(_("admin_4"))
                return
            if remadmin in SUDO_FILTER:
                SUDO_FILTER.remove(remadmin)
                message.reply_text(_("admin_2"))
        except:
            message.reply_text(_("admin_6"))


@Client.on_message(filters.command(["admins"]))
@wrap
def admins(client, message):
    cadmins=list(SUDO_FILTER)
    if message.from_user.id in SUDO_FILTER:
        message.reply_text(
             _("admin_8").format(cadmins)
             )

@Client.on_message(filters.command(["ban"]))
def banuser(client, message):
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
    else:
        if len(message.text.split(" ")) != 2:
            message.reply_text(_("admin_6"))
            return
        try:
            newban = int(message.text.split()[1])
            if newban in SUDO_FILTER:
                message.reply_text(_("admin_6"))
                return
            if newban in BANNED_USERS:
                message.reply_text(_("ban_2"))
                return
            if newban not in BANNED_USERS:
                BANNED_USERS.add(newban)
                message.reply_text(_("ban_1"))
        except:
            message.reply_text(_("admin_6"))

@Client.on_message(filters.command(["unban"]))
def unbanuser(client, message):
    if message.from_user.id not in SUDO_FILTER:
        message.reply_text(_("n4u"))
        return
    if len(message.text.split(" ")) != 2:
        message.reply_text(_("admin_6"))
        return
    try:
        newunban = int(message.text.split()[1])
        if newunban not in BANNED_USERS:
            message.reply_text(_("ban_3"))
            return
        if newunban in BANNED_USERS:
            BANNED_USERS.remove(newunban)
            message.reply_text(_("ban_4"))
    except:
        message.reply_text(_("admin_6"))

@Client.on_message(filters.command(["bannedusers"]))
@wrap
def banneduser(client, message):
    cbans=list(BANNED_USERS)
    if message.from_user.id in SUDO_FILTER:
        message.reply_text(
             _("ban_5").format(cbans)
             )
