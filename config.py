from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

ADMINS = [5554836589, ]
TOKEN = config("TOKEN")
storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


