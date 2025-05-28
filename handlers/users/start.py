from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import start_menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalomu alaykum</b> {message.from_user.full_name}!")
    await message.answer("Bu bot sizga tarjimai hol tayyorlashga yordam  beradi\n buning uchun paastdagi "
                         "buyruqni botga yuboring",reply_markup=start_menu)
