import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('Успешное подключение!')

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY, name TEXT, "
        "direction TEXT, age INTEGER, gruppa TEXT)"
    )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_mentor = random.choice(result)
    await bot.send_message(message.chat.id, f'ID: {random_mentor[0]}\n'
                                            f'Name: {random_mentor[1]}\n'
                                            f'Direction: {random_mentor[2]}\n'
                                            f'Age: {random_mentor[3]}'
                                            f'Group: {random_mentor[4]}')


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()


async def sql_command_get_all_id():
    return cursor.execute("SELECT id FROM mentors").fetchall()