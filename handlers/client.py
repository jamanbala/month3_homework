from aiogram import types, Dispatcher
from config import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Из какога дерева делают спички?'
    answers = [
        'Дуба',
        "Пластик",
        "Стекла",
        "Глины",
        "Осины",
        "Вады"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Лох",
        open_period=10,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def commands(message: types.Message):
    big = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=big)


async def get_random_mentor(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(commands, commands=['mem'])
    dp.register_message_handler(get_random_mentor, commands=['random'])
