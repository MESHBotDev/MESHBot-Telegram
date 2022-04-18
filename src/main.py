from json import load
from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import core.searching_answers as core

with open("package/client.json", "r") as f:
    data = load(f)
bot = Bot(token=data["telegram_token"])
client = Dispatcher(bot)


@client.message_handler(commands=["start", "help", "хелп", "помощь", "гайд"])
async def manual(msg: types.Message):
    with open("package/client_lock.json", "r") as file:
        sys = load(file)
    await msg.answer(f"""Привет, {msg.from_user.first_name}.\nЯ - бот {sys['name']}, решающий задания ЦДЗ.
    \nВК создателя: {sys['vk']}\n(v. {sys['version']})

Для начала работы, отправь мне ссылку на тест и я постараюсь найти ответы.

Если возникла какая-либо проблема, ошибка, баг обратитесь в чат поддержки: {sys['help_place']}.
Там Вам помогут с сложившейся ситуацией.""")


@client.message_handler(commands=['admin', 'analytic'])
async def admin(msg: types.Message):
    with open("analytics.txt", "r") as analytic:
        if msg.from_user.id == 489951151:
            for id_user in analytic.readlines():
                await msg.answer(f'id: {id_user}')
        else:
            await msg.answer("Для начала, отправь ссылку на тест, и я попробую его решить.")


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

    info = f'Text: {msg.text}\nUser: {msg.from_user.get_user_profile_photos}'
    await bot.send_message(489951151, info)
    with open('analitics.txt', '+r') as user_id:
        if str(msg.from_user.id) not in user_id.read():
            user_id.write(f'{msg.from_user.id}\n')


if __name__ == "__main__":
    print(f"Connected at {datetime.today().strftime('%H:%M, %d-%m-%Y')}")
    executor.start_polling(client)
