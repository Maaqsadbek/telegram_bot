from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bolimlar import bolim_tugmalar
from keyboards.inline.Adres_buton import adres_buton_tugmalar
from loader import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="Manzillarni ko'rish")
async def bot_start(call:CallbackQuery):
    await call.message.answer('Sizga qaysi manzilimiz qulay ?',reply_markup = adres_buton_tugmalar)
    await call.answer(cache_time = 60)
