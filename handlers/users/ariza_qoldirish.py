from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.adress import adres_tugmalar
from filters import Admin
from loader import dp
import logging
@dp.message_handler(commands = 'post')
async def postlar(message:types.Message):
    await message.answer(text = 'Iltimos malumotlarni 👇 shu shaklda kiriting.')
    await message.answer(text = "ism familiya\n")
    await message.answer(text = 'Ishlash joyingiz')
    await message.answer(text = 'pasport va ish haqidagi malumotnomaning nusxasi')