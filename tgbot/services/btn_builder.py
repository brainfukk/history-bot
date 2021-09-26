from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def init_buttons_markup(data):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for key, _ in data.items():
        markup.add(KeyboardButton(text=key))
    return markup
