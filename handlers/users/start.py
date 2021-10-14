from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.adress import adres_tugmalar
from filters.shaxsiy import Shaxsiy
from loader import dp,db


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism=message.from_user.full_name
    id=message.from_user.id
    try:
        db.add_user(id, ism)
    except Exception as s:
        print(s)
    await message.answer(f"Asalomualeykum  {message.from_user.full_name}!. Siz Real Kredit Savdo markazinig botiga hush kelibsiz \n"
                         f"iltimos o'zingizga yoqan bo'limni tanlang!" , reply_markup = bolim_tugmalar )
