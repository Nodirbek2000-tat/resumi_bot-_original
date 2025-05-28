from dataclasses import replace

from Tools.scripts.mailerdaemon import emparse_list_from
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS, CHANEL_ID
from loader import dp, bot
from states.anketa import ShogirdState
from keyboards.default.menu import yes_or_no
from keyboards.inline.start_menu_inline import get_admin_button


@dp.message_handler(text="Sherik kerak")
async def shogird_handler(message: types.Message):
    text = """
        <b>Ish joyi topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
        """
    await message.answer(text)
    await message.answer("<b>Ism, familiyangizni kiriting?</b>")
    await ShogirdState.full_name.set()


# full_name state
@dp.message_handler(state=ShogirdState.full_name)
async def full_name_message(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)

    await message.answer("""
                <b>🕑 Yosh: </b>

Yoshingizni kiriting?
Masalan, 19

                """)
    await ShogirdState.age.set()


# age state
@dp.message_handler(state=ShogirdState.age)
async def full_name_message(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)

    await message.answer("""
                        <b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 
Java, C++, C#
                """)
    await ShogirdState.texno.set()


# texno state
@dp.message_handler(state=ShogirdState.texno)
async def full_name_message(message: types.Message, state: FSMContext):
    texno = message.text
    await state.update_data(texno=texno)

    await message.answer("""
                            <b>📞 Aloqa: </b>

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
                """)
    await ShogirdState.aloqa.set()


# texno state
@dp.message_handler(state=ShogirdState.aloqa)
async def full_name_message(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(aloqa=aloqa)

    await message.answer("""
                           <b>🌐 Hudud:</b>

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
                """)
    await ShogirdState.hudud.set()


@dp.message_handler(state=ShogirdState.hudud)
async def full_name_message(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(hudud=hudud)

    await message.answer("""
                        <b>💰 Narxi:</b>


Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
                """)
    await ShogirdState.narx.set()


@dp.message_handler(state=ShogirdState.narx)
async def full_name_message(message: types.Message, state: FSMContext):
    narx = message.text
    await state.update_data(narx=narx)

    await message.answer("""
                        <b>👨🏻‍💻 Kasbi:</b> 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
                """)
    await ShogirdState.kasb.set()


@dp.message_handler(state=ShogirdState.kasb)
async def full_name_message(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data(kasb=kasb)

    await message.answer("""
                  <b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
                """)
    await ShogirdState.murojat.set()


@dp.message_handler(state=ShogirdState.murojat)
async def full_name_message(message: types.Message, state: FSMContext):
    murojat = message.text
    await state.update_data(murojat=murojat)

    await message.answer("""
                    <b>🔎 Maqsad:</b> 

Maqsadingizni qisqacha yozib bering.
                """)
    await ShogirdState.maqsad.set()


@dp.message_handler(state=ShogirdState.maqsad)
async def full_name_message(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(maqsad=maqsad)

    # Ma'lumotlarni oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texno = data.get("texno")
    telegram = f"@{message.from_user.username}"
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narx = data.get("narx")
    kasb = data.get("kasb")
    murojat = data.get("murojat")
    maqsad = data.get("maqsad")

    text = f"""
            <b>Sherik kerak:</b>

🎓 Sherik: {full_name}
🌐 Yosh: {age}
📚 Texnologiya: {texno} 
🇺🇿 Telegram: {telegram}
📞 Aloqa: {aloqa} 
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {murojat} 
🔎 Maqsad: {maqsad} 

#sherik

    """
    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=yes_or_no)
    await ShogirdState.yes_or_no.set()


@dp.message_handler(state=ShogirdState.yes_or_no)
async def confirm_state(message: types.Message, state: FSMContext):
    javob = message.text.lower()

    if javob == "ha":

        # Ma'lumotlarni oqiymiz
        data = await state.get_data()
        full_name = data.get("full_name")
        age = data.get("age")
        texno = data.get("texno")
        telegram = f"@{message.from_user.username}"
        aloqa = data.get("aloqa")
        hudud = data.get("hudud")
        narx = data.get("narx")
        kasb = data.get("kasb")
        murojat = data.get("murojat")
        maqsad = data.get("maqsad")

        text = f"""
                   <b>Sherik kerak:</b>

🎓 Sherik: {full_name}
🌐 Yosh: {age}
📚 Texnologiya: {texno} 
🇺🇿 Telegram: {telegram}
📞 Aloqa: {aloqa} 
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {murojat} 
🔎 Maqsad: {maqsad} 

#sherik


           """

        await message.answer("Adminga yuborildi")
        send_admin = await bot.send_message(
            ADMINS[0],
            text,
            reply_markup=get_admin_button(user_id=int(message.from_user.id),
                                          message_id=int(message.message_id))
        )
        await state.finish()
        await state.update_data(
            {
                "send_message_id": send_admin.message_id,
                "chat_id": send_admin.chat.id
            }
        )

    elif javob == "yo'q":
        await message.answer("Qabul qilinmadi")
        await state.finish()

    else:
        await message.answer("Ha yoki Yo'q tugmasini bosing")


# admin tasdiqlash
@dp.callback_query_handler(lambda c: c.data.startswith(("confirm_", "reject_")))
async def admin_confirm_function(callback: types.CallbackQuery, state: FSMContext):
    action, user_id, message_id = callback.data.split("_")

    # Ma'lumotlarni oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texno = data.get("texno")
    telegram = f"@{callback.from_user.username}"
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narx = data.get("narx")
    kasb = data.get("kasb")
    murojat = data.get("murojat")
    maqsad = data.get("maqsad")

    text = f"""
    <b>Sherik kerak:</b>

🎓 Xodim: {full_name}
🌐 Yosh: {age}
📚 Texnologiya: {texno} 
🇺🇿 Telegram: {telegram}
📞 Aloqa: {aloqa} 
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {murojat} 
🔎 Maqsad: {maqsad} 

#sherik


       """

    if action == "confirm":
        await bot.send_message(
            chat_id=CHANEL_ID,
            text=text
        )
        #         foydalanuvchiga xabar beramiz
        await bot.send_message(
            chat_id=user_id,
            text="Sizning arizangiz tasdiqlandi"
        )
        #         Adminga tasdiqlanganini bildiramiz
        await callback.message.edit_text(
            text=f"{text}\n\n ✅Tasdiqlandi va kanalga yuborildi"
        )

    elif action == "reject":
        await bot.send_message(
            chat_id=user_id,
            text="Sizning arizangiz rad etildi"

        )

        await callback.message.edit_text(
            text=f"{text}\n\n ❌Rad etildi"
        )
        await callback.answer()






