from aiogram.utils import executor
from config import dp
from handlers import client, extra, callback

client. register_handlers_client(dp=dp)
callback. register_handlers_callback(dp=dp)
extra. register_handlers_extra(dp=dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
