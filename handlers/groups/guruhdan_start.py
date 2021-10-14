from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.adress import adres_tugmalar
from filters import Group
from loader import dp


@dp.message_handler(Group(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Asalomualeykum  {message.from_user.full_name}!. Siz Real Kredit Savdo markazinig botiga hush kelibsiz \n"
                         f"iltimos o'zingizga yoqan bo'limni tanlang!" ),
    try:
        await message.answer('siz guruhdan murojat qildingiz', reply_markup = bolim_tugmalar )
    except:
        print('groupda ishlamadi')
