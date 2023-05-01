from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config
from aiogram import Bot, Dispatcher
TOKEN = config('TOKEN')

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (1437964455,)
