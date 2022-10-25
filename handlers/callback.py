from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from database.bot_db import sql_command_delete


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
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

        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Очкошник",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Какое группа самое сильное?"
    answers = [
        "22-1",
        "22-3",
        "22-2"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам выбирай",
        open_period=10
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Удален из БД', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))
