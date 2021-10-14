from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import kanallar
from keyboards.inline.bolimlar import bolim_tugmalar
from utils.misc import azo_bolish
from loader import bot
import logging

class Asosiy(BaseMiddleware):
    async def on_pre_process_update(self, update: types.update, data: dict):
        if update.message:
            user=update.message.from_user.id
            logging.info(user)
        elif update.callback_query:
            user = update.callback_query.message.from_user.id
        else:
            return
        resault='botdan foydalanish uchun quyidagi kanallarga obuna bo\'ling:\n'
        finaly_status=True
        for chanel in kanallar:
            status=await azo_bolish.azolik(user_id = user,
                                           channel = chanel)
            finaly_status*=status
            chanel=await bot.get_chat(chanel)
            if not status:
                invite_link=await chanel.export_invite_link()
                resault+=(f"👉 <a href='{invite_link}'> {chanel.title} </a> \n")
        if not finaly_status:
            await update.message.answer(resault, disable_web_page_preview = True)

            raise CancelHandler()


