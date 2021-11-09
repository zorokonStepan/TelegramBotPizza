import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import json

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_start_up(_):
    print('Бот вышел в онлайн')


# *****************************Клиентская часть**************************************************************
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Добро пожаловать!")
        await message.delete()
    except:
        await message.reply('Ощение с ботом через ЛС, напишите ему:\nhttps://t.me/T_y_P_aBot')


@dp.message_handler(commands=['operating_mode'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00')


@dp.message_handler(commands=['address'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Площадь Мужества, 17")


# @dp.message_handler(commands=["menu"])
# async def pizza_menu_command(message: types.Message):
#     for ret in cur.execute('SELECT*FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


# ******************************Админская часть**************************************************************
# ********************************Общая часть****************************************************************

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
