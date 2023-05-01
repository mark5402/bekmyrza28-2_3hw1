from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


# from . import _kb
# from database.bot_db import sql_command_insert


# FSM - Finite State Machine
class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    id = State()
    group = State()
    direction = State()
    # submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.name.set()
        await message.answer("Как зовут??")
    else:
        await message.answer("Пиши в личку!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["telegram_id"] = message.from_user.id
        data["username"] = message.from_user.username
        data["name"] = message.text
    print(data)
    await FSMAdmin.next()
    await message.answer("Скока лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 16 < int(message.text) < 60:
        await message.answer("Возрастное ограничение!")
    else:
        async with state.proxy() as data:
            data["age"] = message.text
        await FSMAdmin.next()
        await message.answer("put you id number?")


async def load_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data["id"] = message.text
        await FSMAdmin.next()
        await message.answer("write your group number ?")


async def load_group(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data["group"] = message.text
        await FSMAdmin.next()
        await message.answer("write your  direction?")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["direction"] = message.text
    await message.answer(f'Иеформация о менторе:\n'
                         f'name - {data["name"]}\n'
                         f'age - {data["age"]}\n'
                         f'id - {data["id"]}\n'
                         f'group - {data["group"]}\n'
                         f'direction - {data["direction"]}')
    await FSMAdmin.next()
    await message.answer("все ли верно?")


async def submit_state(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # await sql_command_insert(state)
        await state.finish()
        await message.answer("Все свободен)")
    if message.text.lower() == "заново":
        await FSMAdmin.name.set()
        await message.answer("Как звать??")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Ну и пошел ты!")



#
#
#
# async def submit_state(message: types.Message, state: FSMContext):
#     if message.text.lower() == "да":
#         # await sql_command_insert(state)
#         await state.finish()
#         await message.answer("Все свободен)")
#     if message.text.lower() == "заново":
#         await FSMAdmin.name.set()
#         await message.answer("Как звать??")
#
#
# async def cancel_reg(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state:
#         await state.finish()
#         await message.answer("Ну и пошел ты!")
#

def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['start'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
