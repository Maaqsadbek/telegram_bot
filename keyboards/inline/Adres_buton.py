from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

adres_buton_tugmalar = InlineKeyboardMarkup(
    inline_keyboard = [

        [
            InlineKeyboardButton(text = "Toshloq tumani", callback_data = "Toshloq tumani"),
            InlineKeyboardButton(text = "Qo'shtepa tumani", callback_data = "Qo'shtepa tumani")
        ],
    ],
    resize_keyboard = True

)