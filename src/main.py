from json import load
from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import core.searching_answers as core


with open("package/client.json", "r") as f:
    data = load(f)
client = Dispatcher(Bot(token=data["telegram_token"]))

@client.message_handler(commands=["start", "help", "хелп", "помощь", "гайд"])
async def manual(msg: types.Message):
    with open("package/client_lock.json", "r") as f:
        sys = load(f)
    await msg.answer(f"""Привет, {msg.from_user.first_name}.\nЯ - бот {sys['name']}, решающий задания ЦДЗ. (v. {sys['version']})

Для начала работы, отправь мне ссылку на тест и я постараюсь найти ответы.

Доп. информация:
• Исходный код бота: {sys['github_link']}""")

@client.message_handler(content_types=["text"])
async def get_text_messages(msg: types.Message):
    if msg.text.startswith("http"):
        answers = core.get_answers(link=msg.text)
        try:
            for task_number, task in enumerate(answers):
                await msg.answer(f"Вопрос №{task_number + 1}: {task[0]}\n\nОтвет: {task[1]}")
        except:
            await msg.answer(answers)
    else:
        await msg.answer("Для начала, отправь ссылку на тест, и я попробую его решить.")

if __name__ == "__main__":
    print(f"Connected at {datetime.today().strftime('%H:%M, %d-%m-%Y')}")
    executor.start_polling(client)
