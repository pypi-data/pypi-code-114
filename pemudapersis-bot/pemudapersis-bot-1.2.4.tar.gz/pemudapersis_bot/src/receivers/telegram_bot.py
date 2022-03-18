""" Pemuda Persis bot on Telegram """

import logging
import os
from typing import Tuple, Optional
from telegram import Update, ForceReply, ParseMode, ChatMember, ChatMemberUpdated, Chat
from telegram.error import BadRequest
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ChatMemberHandler,
)

from pemudapersis_bot.src.configs.environment import EnvConfig as Config
from pemudapersis_bot.src.models.chat import Chat as ChatData
from pemudapersis_bot.src.services.chat_handler import ChatHandler
from pemudapersis_bot.src.services.api_handler import APIHandler

# Enable logging
logging.basicConfig(format=Config.LOG_FORMAT, level=Config.LOG_LEVEL)

HANDLER = ChatHandler()
API_HANDLER = APIHandler()
HELP = """📜 Petunjuk penggunaan :

Petunjuk penggunaan Chatbot..
"""
NEW_MEMBERS = {}


def start_command(update: Update, context: CallbackContext = None) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        f"Assalamualaikum {user.mention_markdown_v2()}\! Silahkan masukan NPA antum\.",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext = None) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(HELP)


def contact_command(update: Update, context: CallbackContext = None) -> None:
    """Send a message when the command /contact is issued."""
    update.message.reply_text("Pertanyaan atau saran bisa hubungi @Admin")


def handler(update: Update, context: CallbackContext = None) -> None:
    """Method for handling messages"""
    logging.debug(NEW_MEMBERS)
    chat_user_id = update.message.from_user.id
    if (
        update.effective_chat.type in [Chat.GROUP, Chat.SUPERGROUP]
        and chat_user_id not in NEW_MEMBERS.keys()
    ):
        return
    elif chat_user_id in NEW_MEMBERS.keys() and len(update.message.text) != 7:
        update.message.reply_text("Format NPA salah. Silahkan coba lagi!!")
        return
    elif chat_user_id in NEW_MEMBERS.keys():
        npa_status = API_HANDLER.check_npa(npa=update.message.text)
        if npa_status == "Valid":
            NEW_MEMBERS.pop(chat_user_id)
            update.message.reply_text("NPA Valid. Selamat bergabung di Group Akhi!")
            return
        elif NEW_MEMBERS.get(chat_user_id) == 3:
            update.message.reply_text(
                "Tiga kali gagal verifikasi. Afwan, antum tidak diperbolehkan memposting apapun di Group ini (Banned)!"
            )
            update.effective_chat.ban_member(chat_user_id)
            return
        elif NEW_MEMBERS.get(chat_user_id) == 2:
            update.message.reply_text(
                "NPA Tidak Valid. Silahkan coba lagi! Kesempatan terakhir."
            )
            NEW_MEMBERS[chat_user_id] = NEW_MEMBERS.get(chat_user_id) + 1
            return
        else:
            update.message.reply_text("NPA Tidak Valid. Silahkan coba lagi!")
            NEW_MEMBERS[chat_user_id] = NEW_MEMBERS.get(chat_user_id) + 1
            return

    if update.message.text[0] == "!":
        reply = HANDLER.magic_keyword(update.message.text)
        update.message.reply_text(reply)
        return

    if update.message.from_user.username:
        sender_id = update.message.from_user.username
    else:
        sender_id = "unknown"

    chat = ChatData(
        chat_id=update.message.chat_id,
        sender_id=sender_id,
        sender=update.message.from_user.first_name,
        str_message=update.message.text,
    )
    reply = HANDLER.handler(chat)
    try:
        logging.debug("Sending message...")
        update.message.reply_text(reply)
    except BadRequest:
        update.message.reply_text("Afwan, ana belum paham soal itu.")
    logging.debug("Message sent..")


def extract_status_change(
    chat_member_update: ChatMemberUpdated,
) -> Optional[Tuple[bool, bool]]:
    """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    the status didn't change.
    """
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get(
        "is_member", (None, None)
    )

    if status_change is None:
        return None

    old_status, new_status = status_change
    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.CREATOR,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.CREATOR,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    return was_member, is_member


def greet_chat_members(update: Update, context: CallbackContext) -> None:
    """Greet new users in chats"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        NEW_MEMBERS[update.chat_member.from_user.id] = 0
        update.effective_chat.send_message(
            f"Ahlan wa sahlan {member_name}. Untuk verifikasi, silahkan reply pesan ini dengan NPA antum!",
            parse_mode=ParseMode.HTML,
        )
    # elif was_member and not is_member:
    #     update.effective_chat.send_message(
    #         f"{member_name} is no longer with us. Thanks a lot, {cause_name} ...",
    #         parse_mode=ParseMode.HTML,
    #     )


def start_bot():
    """Start the bot."""
    # Create the Updater and pass your bot's token.
    if os.environ.get("BOT_TOKEN"):
        token = os.environ["BOT_TOKEN"]
    else:
        logging.error("BOT_TOKEN is not set!")
        return

    updater = Updater(token)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("contact", contact_command))

    # in Group handlers
    dispatcher.add_handler(
        ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER)
    )

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handler))

    # Start the Bot
    updater.start_polling(allowed_updates=Update.ALL_TYPES)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    start_bot()
