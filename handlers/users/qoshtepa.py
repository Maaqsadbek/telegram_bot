from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.Adres_buton import adres_buton_tugmalar
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(text="Qo'shtepa tumani")
async def bot_start(call:CallbackQuery):
    await call.message.answer("Qo'shtepa tumani Sarmazor MFY. Shijoatkor ko'chasi 88-uy")

