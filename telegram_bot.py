from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

from kb import kb, ikb

import parser_google
import os
import hashlib


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

data = None

text_start = '''
Добро пожаловать в <b>Google Bot</b> 👽
<em>К вашему вниманию список команд</em>:
<b>/description</b> - <em>описание бота🤖</em>
<b>/find</b> - <em>поиск во всех щелях интернета👀</em>
'''

text_description = '''
Наш бот может искать информацию в интернете! <b>Любую</b> 🥵
'''

text_find = '''
<em>Напишите то, что хотите отыскать!</em>
'''


async def on_startup(_):
    print('Я включился)')


@dp.message_handler(commands=['Start'])
async def cmd_start(message: types.Message):
    await message.answer(text=text_start, parse_mode='HTML')
    await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgEAAxkBAAEHMGRjvEojvP16zE29RJN1XcfqtldU6gACIQIAAh9IMEcPta5LcPd07i0E', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_start(message: types.Message):
    await message.answer(text=text_description, parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['find'])
async def cmd_start(message: types.Message):
    await message.answer(text=text_find, parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.callback_query_handler()
async def callback_data(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('Огонь🔥')
    if callback.data == 'dislike':
        await callback.answer('Фуу🤢')


@dp.inline_handler()
async def inline_bot(inline_handler: types.InlineQuery):
    text = inline_handler.query or None
    if text != None:
        result_id: str = hashlib.md5(text.encode()).hexdigest()
        print('вход')
    else:
        print('Значение ввода None')
    get_data(text)
    input_content = InputTextMessageContent(data)
    item = InlineQueryResultArticle(input_message_content=input_content, id=result_id, title='Search', description='default..')

    await bot.answer_inline_query(results=[item], inline_query_id=inline_handler.id, cache_time=1)



@dp.message_handler()
async def send_data(message: types.Message):
    get_data(message.text)
    await message.answer(data, reply_markup=ikb)


def get_data(text):
    global data
    parser_google.get_url(text)
    parser_google.get_data(parser_google.response)
    with open('google.txt', encoding='utf-8') as file:
        data = file.read()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
