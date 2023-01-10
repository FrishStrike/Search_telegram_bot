from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('/description')
b2 = KeyboardButton('/find')

kb.add(b1, b2)


ikb = InlineKeyboardMarkup()

ib1 = InlineKeyboardButton(text='👍', callback_data='like')
ib2 = InlineKeyboardButton(text='👎', callback_data='dislike')

ikb.add(ib1, ib2)
