from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot

# @dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_2_button")
    markup.add(button_1)

    question2 = "Столица Кыргызстана?!"
    answer2 = [
        "Bishkek",
        "Osh",
        "Jalal-Abad",
        "Cholpon-Ata"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question2,
        options=answer2,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="тип",
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("MEMES", callback_data="memes_button")
    markup.add(button)

    question2 = "Площадь Кыргызстана!"
    answer2 = [
        "201 100",
        "199 900",
        "17 780",
        "18 990"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question2,
        options=answer2,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="ай ай ай",
        reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="quiz_1_button")
    dp.register_callback_query_handler(quiz_3, text="quiz_2_button")
