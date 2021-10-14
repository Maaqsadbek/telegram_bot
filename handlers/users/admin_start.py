from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.adress import adres_tugmalar
from filters import Admin
from loader import dp


@dp.message_handler(Admin(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Asalomualeykum admin botga xush kelibsiz  {message.from_user.full_name}!. Siz Real Kredit Savdo markazinig botiga hush kelibsiz \n"
                         f"iltimos o'zingizga yoqan bo'limni tanlang!" , reply_markup = bolim_tugmalar )
