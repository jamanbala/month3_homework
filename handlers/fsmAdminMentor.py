from aiogram import types, Dispatcher
from config import bot
from keyboard.client_cb import cancel_markup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer(f'Привет {message.from_user.full_name}\n'
                             f'Введи айди ментора')
    else:
        await message.answer('Пиши в личку')


async def load_id(message: types.Message, state: FSMContext):
    try:
        mentor_id = int(message.text)
        if mentor_id < 0 or mentor_id > 100000000:
            await message.answer('Неправильное айди')
        else:
            async with state.proxy() as data:
                data['ID'] = mentor_id
            await FSMAdmin.next()
            await message.answer('Введите имя ментора', reply_markup=cancel_markup)
    except:
        await message.answer('Айди может быть только из цифр')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Введите направление ментора', reply_markup=cancel_markup)


async def load_dir(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dir'] = message.text
    await FSMAdmin.next()
    await message.answer('Введите возраст ментора', reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 12 or age > 60:
            await message.answer('Такого ментора не бывает\nВведите нормальные возраст', reply_markup=cancel_markup)
        else:
            async with state.proxy() as data:
                data['age'] = age
            await FSMAdmin.next()
            await message.answer('Введите группу ментора', reply_markup=cancel_markup)
    except:
        await message.answer('Возраст должке состоять только из цифр', reply_markup=cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"ID: {data['ID']} Имя: {data['name']}\n"
                             f"Направление: {data['dir']} Возраст: {data['age']} Группа: {data['group']}")
    await sql_command_insert(state)
    await state.finish()
    await message.answer('Регистрация закончена!')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты нах")
    else:
        await message.answer('Ты не регистрируешься')


def register_handlers_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_dir, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)


