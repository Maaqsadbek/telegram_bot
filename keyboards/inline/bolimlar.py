from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bolim_tugmalar=InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '💻 Televizorlar 💻', url = 'https://t.me/real_kredit_televizorlar'),
            InlineKeyboardButton(text = '📱 Telefonlar 📱', url= 'https://t.me/real_kredit_telefonlar'),
            InlineKeyboardButton(text = '❄️Xolodilniklar❄️', url = 'https://t.me/real_kredit_xolodilniklar'),


        ],
        [
            InlineKeyboardButton(text= '🌊 Kir yuvish mashinalari 🌊', url = 'https://t.me/real_kredit_kir_yuvis_mashinalar'),
            InlineKeyboardButton(text= '🥐 Mini pechlar 🥯', url = 'https://t.me/real_kredit_mini_pechlar'),
            InlineKeyboardButton(text= '🍽 Kichik oshxona jixozlari 🍴', url = 'https://t.me/real_kredit_MBT')
        ],
        [
            InlineKeyboardButton(text = '🚲 Velosipedlar 🏍', url = 'https://t.me/real_kredit_kir_yuvis_mashinalar')
        ],
        [
            InlineKeyboardButton(text = "👑 Shoxona mebellar 👑", url = "https://t.me/real_kredit_mebellar" )
        ],
        [
            InlineKeyboardButton(text = "Manzillarni ko'rish", callback_data = "Manzillarni ko'rish")
        ]
    ],
        resize_keyboard = True

)