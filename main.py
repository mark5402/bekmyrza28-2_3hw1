from aiogram import types, Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)




# @dp.message_handler(commands=['start'])
# async def echo(message:types.Message):
    # await message.answer('Salam bro')
    # await message.reply('Salam brother it is some kind of me')



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT", callback_data="quiz1_button")
    markup.add(button1)
    question1 = "Кто выйграл ЧМ 2022?"
    answer1 = [
        "Англия",
        "Франция",
        "Бразилия",
        "Аргенитина",
        "Германия",
        "Испания"

    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question1,
        options=answer1,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="футбол не твое",
        reply_markup=markup,
    )


@dp.message_handler(commands=['quiz2'])
async def quiz_2(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT", callback_data="quiz2_button")
    markup1.add(button2)
    question2 = "Столица Кыргызстана?!"
    answer2 = [
        "Bishkek",
        "Osh",
        "Jalal-Abad",
        "Cholpon-Ata"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question2,
        options=answer2,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="down man",
        reply_markup=markup1
    )


@dp.message_handler(commands=['memes'])
async def echo(message:types.Message):
    photo = open('memes/i.webp', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo, caption='trick or treat!')


@dp.message_handler()
async def echo(message:types.Message):
    # print(type(message.from_user.id))
    # print(type(message.text))
    if message.text.isalpha():
        # await message.answer('ttt')
        await bot.send_message(chat_id=message.from_user.id, text=message.text)
    else:
        item = message.text
        item = int(item)
        await message.answer(item * item)




# @dp.message_handler(lambda message: message.text == 'Я ее знаю!' or message.text == 'Теперь я знаю!')
# async def weight_know(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Тогда проинформируйте меня.\n\nP.S. пишите только числа, без физических величин, иначе конечный результат приведет к ошибке. [Последующих вопросов это тоже касается].')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
