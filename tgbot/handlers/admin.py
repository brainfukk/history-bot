from aiogram import Dispatcher
from aiogram.types import Message, ParseMode

from tgbot.models.dialog import Dialog
from tgbot.models.role import UserRole
from tgbot.services.btn_builder import init_buttons_markup
from tgbot.services.fake_db import DatabaseFaker

DB_DATA = DatabaseFaker.get_data()
markup = init_buttons_markup(DB_DATA)


def get_full_name(m: Message):
    fn = "" if m.from_user.first_name is None else m.from_user.first_name
    ln = "" if m.from_user.last_name is None else m.from_user.last_name
    return "{} {}".format(fn, ln).strip()


async def admin_start(m: Message):
    await m.reply(
        Dialog.WELCOME.value.format(get_full_name(m)),
        reply_markup=markup,
        parse_mode=ParseMode.HTML,
    )


async def handle_text(m: Message):
    await m.bot.send_message(
        chat_id=m.from_user.id,
        text="{} {}".format("Hey👋, there is your text!\n\n", DB_DATA.get(m.text)),
        reply_markup=markup,
    )


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"], state="*", role=[UserRole.ADMIN, UserRole.USER]
    )
    dp.register_message_handler(
        handle_text,
        lambda msg: msg.text in list(DB_DATA.keys()),
        state="*",
        role=[UserRole.ADMIN, UserRole.USER],
    )
    # # or you can pass multiple roles:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", role=[UserRole.ADMIN])
    # # or use another filter:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
