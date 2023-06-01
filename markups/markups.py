from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ---main menu---
btnStart = KeyboardButton('🚀START🚀')
btnSite = KeyboardButton('Site🦠')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStart, btnSite)
