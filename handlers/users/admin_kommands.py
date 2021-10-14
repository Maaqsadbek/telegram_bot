import asyncio
from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import db,dp, bot
@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users=db.select_all_users()

    await message.answer(users)
@dp.message_handler(text="/reklama", user_id=ADMINS)
async def sent_ad_to_all(message: types.Message, state: FSMContext):
    users=db.select_all_users()
    for user in users:
        user_id=user[0]
        await bot.send_message(chat_id = user_id, text = 'python news1 kanaliga obuna boling')
        await asyncio.sleep(00.5)