from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


# @dp.message_handler(commands=['memes'])
async def memes(message: types.Message):
    photo = open('memes/ocr.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo, caption='trick or treat')


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

    question = "Кто выйграл ЧМ 2022?"
    answer = [
        "Англия",
        "Франция",
        "Бразилия",
        "Аргенитина",
        "Германия",
        "Испания",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        explanation="Дурачок",
        open_period=10,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(memes, text="memes_button")
