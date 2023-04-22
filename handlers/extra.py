from aiogram import types, Dispatcher
import random
from config import bot, ADMINS


async def echo(message: types.Message):
    # await message.answer('number')
    if message.from_user.id in ADMINS:
        if message.text.isdigit():
            await message.answer(int(message.text) ** 2)

        emoji = ['⚽️', '🎰', '🎧', '🎳', '🎯', '🎲', '🏀']
        sended_emoji = random.choice(emoji)
        if message.text.startswith('game'):
            await message.answer_dice(emoji=sended_emoji)
        if message.reply_to_message:
            await message.answer('pinned')
            await message.pin()
    else:
        await message.answer('nein')

    # else:
    #     await message.answer(text=message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
    # dp.register_message_handler(pinnig)
    # dp.register_message_handler(pin_message)
    # dp.register_message_handler(game_message, commands='game')
