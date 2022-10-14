from aiogram import types
from aiogram.utils import executor
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Привет')


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Кто больше всех кричит, а меньше всех делает?'
    answers = [
        "Маряк",
        "Путин",
        "Начальник",
        "Пацан",
        "Мама",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Очкошник",
        open_period=10,
        reply_markup=markup
    )


@dp.message_handler(commands=['mem'])
async def commands(message: types.Message):
    big = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=big)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
