import asyncio
from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import callback, extra, client, fsmAdminMentor, admin
from handlers import callback, extra, client, fsmAdminMentor, admin, notifications,inine
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

inine.register_handlers_inline(dp)
notifications.register_handlers_notifications(dp)
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsmadmin(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
