from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


start_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rezumi qilish")
        ],
    ],
    resize_keyboard=True
)

yes_or_no=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)