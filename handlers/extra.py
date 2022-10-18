from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)