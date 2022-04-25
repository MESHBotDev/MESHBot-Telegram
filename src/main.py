from json import load
from datetime import datetime
import time
from functools import lru_cache

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import core.searching_answers as core

with open("package/client.json", "r") as telegram_data:
    data = load(telegram_data)
bot = Bot(token=data["telegram_token"])
client = Dispatcher(bot)
admin_id = 489951151
katya_id = 857280061


def analytics(message: types.Message):
    with open('analytics.txt', '+r') as user_id:
        if str(message.from_user.id) not in user_id.read():
            user_id.write(f'{message.from_user.id, message.from_user.username}\n')


@client.message_handler(commands=["start", "help", "хелп", "помощь", "гайд"])
async def manual(msg: types.Message):
    with open("package/client_lock.json", "r") as file:
        sys = load(file)
    await msg.answer(f"""Привет, {msg.from_user.first_name}.\nЯ - бот {sys['name']}, решающий ЦДЗ.(v. {sys['version']})
    \nВК создателя: {sys['vk']}\n
Для начала работы, отправь мне ссылку на тест и я постараюсь найти ответы.\n
Если возникла какая-либо проблема, ошибка, баг обратитесь в чат поддержки: {sys['help_place']}.
Там Вам помогут с сложившейся ситуацией.""")
    analytics(msg)


@client.message_handler(commands=['admin', 'analytics'])
async def admin(msg: types.Message):
    with open("analytics.txt", "r") as analytic:
        if msg.from_user.id == admin_id or msg.from_user.id == katya_id:
            counter = 0
            for number, id_user in enumerate(analytic.readlines()):
                await msg.answer(f'{number+1}. User: {id_user}')
                counter += 1
            await msg.answer(f'Всего пользователей: {counter}')
        else:
            await msg.answer("Для начала, отправь ссылку на тест, и я попробую его решить.")


@lru_cache(None)
@client.message_handler(content_types=["text"])
async def get_text_messages(msg: types.Message):
    if msg.text.startswith("http"):
        result_answers = []
        start_time = time.time()
        await msg.answer("Начал решать...")
        try:
            for all_answers in range(25):
                answers = core.get_answers(link=msg.text)
                for answer in answers:
                    while answer not in result_answers:
                        result_answers.append(answer)
        except:
            # await msg.answer(''.join(result_answers))
            await msg.answer('Хм странно, но я ничего не нашел. Проверь правильность ссылки или нажми /help')
        try:
            for task_number, task in enumerate(result_answers):
                await msg.answer(f"Вопрос №{task_number + 1}: {task[0]}\n\nОтвет: {task[1]}")
            await msg.answer(f"Решено за {'%s секунд' % round((time.time() - start_time), 1)}")
        except:
            await msg.answer(''.join(result_answers))
    else:
        await msg.answer("Для начала, отправь ссылку на тест, и я попробую его решить.")
    info = f'Text: {msg.text}\nUser: {msg.from_user.get_user_profile_photos}'
    await bot.send_message(admin_id, info)
    analytics(msg)


if __name__ == "__main__":
    print(f"Connected at {datetime.today().strftime('%H:%M, %d-%m-%Y')}")
    executor.start_polling(client)
