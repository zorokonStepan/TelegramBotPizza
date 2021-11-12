from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
# для хранения данных в оперативной памяти
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
