from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/T_y_P_aBot')


# @dp.message_handler(commands=['режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['адрес'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Площадь Мужества, 17")


@dp.message_handler(commands=["меню"])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['адрес'])
    dp.register_message_handler(pizza_menu_command, commands=['меню'])
