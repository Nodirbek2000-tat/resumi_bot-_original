from aiogram import types
from frozenlist import FrozenList

from loader import dp,bot
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import start_menu,yes_or_no
from states.rezumi import Rezumi

# 📝 Resume Bot uchun savollar ro‘yxati:
# Ismingiz nima?
# (Masalan: Nodirbek Karimov)
#
# Tug‘ilgan sanangiz yoki yoshingiz nechchida?
# (Masalan: 2007-yil 10-mart / 18 yosh yoki 18.10.2007-yil)
#
# Yashash joyingiz (manzil)?
# (Masalan: Samarqand, O‘zbekiston)
#
# Telefon raqamingiz va email manzilingizni yozing:
# (Masalan: +99890..., email@example.com)
#
# Ma’lumotingiz darajasi va o‘qigan o‘quv yurtlaringiz:
# (Masalan: Samarqand IT Texnikumi, 2022–2025)
#
# Kasbiy maqsadingiz yoki professional maqsadingiz:
# (Masalan: Web dasturchi sifatida ishlashni istayman)
#
# Ish tajribangiz bo‘lsa, qayerda va nima qilib ishlagansiz?
# (Masalan: 2024-yil “TechSoft”da amaliyotchi dasturchi bo‘lib ishladim)
#
# Biladigan texnologiyalar yoki ko‘nikmalaringiz (skills):
# (Masalan: HTML, CSS, JavaScript, Python, Git, Figma, Canva, Word, Excel)
#
# Tillarni bilish darajangiz:
# (Masalan: O‘zbek tili – ona tili, Ingliz tili – B2, Rus tili – boshlang‘ich)
#
# Sertifikatlaringiz bo‘lsa, ularni yozing:
# (Masalan: IELTS 6.5, Udemy kurslari, IT Markazi sertifikati va h.k.)
#
# Qiziqishlaringiz va hobbilaringiz:
# (Masalan: Kitob o‘qish, dizayn, coding, sport)
#
# Ijtimoiy tarmoqlardagi profilingiz (agar qo‘shmoqchi bo‘lsangiz):
# (Masalan: LinkedIn, GitHub, Telegram, Instagram)

@dp.message_handler(text="Rezumi qilish")
async def rezumi_function(message:types.Message):
    text="""        <b>Rezumi qilish uchun ariza berish</b>
Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. """

    await message.answer(text)
    await message.answer("""<b> Ismingiz nima?</b>
(Masalan: Nodirbek Karimov)""")

    await Rezumi.full_name.set()

# full_name state for bot

@dp.message_handler(state=Rezumi.full_name)
async def full_name(message:types.Message,state:FSMContext):
    name=message.text
    await state.update_data(ism=name)

    await message.answer("""<b>Tug‘ilgan sanangiz yoki yoshingiz nechchida?</b>
(Masalan: 2007-yil 10-mart / 18 yosh yoki 18.10.2007-yil)""")

    await Rezumi.age.set()

# fucntion for age
@dp.message_handler(state=Rezumi.age)
async def age_function(message:types.Message,state:FSMContext):
    age=message.text
    await state.update_data(yosh=age)

    await message.answer("""<b>Yashash joyingiz (manzil)?</b>
(Masalan: Samarqand, O‘zbekiston)""")
    await Rezumi.home.set()

# this function is for home
@dp.message_handler(state=Rezumi.home)
async def home_function(message:types.Message,state:FSMContext):
    text=message.text
    await state.update_data(manzil=text)


    await message.answer("""<b>Telefon raqamingiz va email manzilingizni yozing:</b>
(Masalan: +99890..., email@example.com)""")
    await Rezumi.number.set()


# this function is for number
@dp.message_handler(state=Rezumi.number)
async def number_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(raqam=text)

    await message.answer("""<b>Ma’lumotingiz darajasi va o‘qigan o‘quv yurtlaringiz:</b>
(Masalan: Samarqand IT Texnikumi, 2022–2025)""")
    await Rezumi.information_degre.set()


# this function is for information_degre
@dp.message_handler(state=Rezumi.information_degre)
async def info_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(malumotlar_darajasi=text)

    await message.answer("""<b>Kasbiy maqsadingiz yoki professional maqsadingiz:</b>
(Masalan: Web dasturchi sifatida ishlashni istayman)""")
    await Rezumi.purpose.set()


# this function is for purpose
@dp.message_handler(state=Rezumi.purpose)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(maqsad=text)

    await message.answer("""<b>Ish tajribangiz bo‘lsa, qayerda va nima qilib ishlagansiz?</b>
(Masalan: 2024-yil “TechSoft”da amaliyotchi dasturchi bo‘lib ishladim)""")
    await Rezumi.excperience.set()

# this function is for excperince
@dp.message_handler(state=Rezumi.excperience)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(tajriba=text)

    await message.answer("""<b>Biladigan texnologiyalar yoki ko‘nikmalaringiz (skills):</b>
(Masalan: HTML, CSS, JavaScript, Python, Git, Figma, Canva, Word, Excel)""")

    await Rezumi.technologia.set()

# this function is for technologia
@dp.message_handler(state=Rezumi.technologia)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(technologiya=text)


    await message.answer("""<b>Tillarni bilish darajangiz:</b>
(Masalan: O‘zbek tili – ona tili, Ingliz tili – B2, Rus tili – boshlang‘ich)""")
    await Rezumi.language.set()

# this function is for language
@dp.message_handler(state=Rezumi.language)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(tillar=text)

    await message.answer("""<b>Sertifikatlaringiz bo‘lsa, ularni yozing:</b>
(Masalan: IELTS 6.5, Udemy kurslari, IT Markazi sertifikati va h.k.)""")
    await Rezumi.certificate.set()

# this function is for certificate
@dp.message_handler(state=Rezumi.certificate)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(sertifikat=text)

    await message.answer("""<b>Qiziqishlaringiz va hobbilaringiz:</b>
(Masalan: Kitob o‘qish, dizayn, coding, sport)""")
    await Rezumi.interests.set()

# this function is for interests
@dp.message_handler(state=Rezumi.interests)
async def purpose_function(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(qiziqishlar=text)


#     barcha malumotlar shu yerda
    data=await state.get_data()
    full_name=data.get("ism")
    age=data.get("yosh")
    ceit=data.get("manzil")
    num=data.get("raqam")
    info=data.get("malumotlar_darajasi")
    purpose=data.get("maqsad")
    excperince=data.get("tajriba")
    technologiya=data.get("technologiya")
    language=data.get("tillar")
    certificate=data.get("sertifikat")
    interests=data.get("qiziqishlar")

    result=f"""

👨🏻‍💻To‘liq ism va familiya: {full_name}
🕑Tug‘ilgan sana / Yosh: {age}
Yashash joyi: {ceit}
Aloqa ma’lumotlari: {num}
Ma’lumotlar: {info}
Kasbiy maqsadlar: {purpose}
Ish tajriba (agar bo‘lsa): {excperince}
Ko‘nikma va bilimlar: {technologiya}
Tillarni bilish darajasi: {language}
Sertifikat va diplomlar: {certificate}
Qiziqishlar va hobbilar: {interests}


"""
    await message.answer(result)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=yes_or_no)
    await Rezumi.yes_or_no.set()



@dp.message_handler(state=Rezumi.yes_or_no)
async def yes_or_no(message:types.Message,state:FSMContext):
    javob=message.text.lower()

    # if javob=="ha":

































