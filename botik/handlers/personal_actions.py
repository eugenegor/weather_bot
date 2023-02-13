from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(is_owner=True, commands=["setlink"])
async def setlink_command(message: types.Message):
    with open("link.txt", "w+") as f:
        f.write(message.text.replace("/setLink ", "").strip())
        f.close()

    await message.answer("Ссылка успешно сохранена!")    

@dp.message_handler(is_owner=True, commands=["getlink"])
async def setlink_command(message: types.Message):
    with open("link.txt", "r") as f:
        content = f.readlines()
        f.close()

    await message.answer("Текущая ссылка: {}" .format(content[0].strip()))            