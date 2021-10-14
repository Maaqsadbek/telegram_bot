from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


adres_tugmalar=InlineKeyboardMarkup(
    inline_keyboard = [

        [
            InlineKeyboardButton(text = "Manzillarni ko'rish", callback_data = " " )
        ],
    ],
        resize_keyboard = True

)