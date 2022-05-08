from json import load
from datetime import datetime
import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import core.searching_answers as core

with open("package/client.json", "r") as telegram_data:
    data = load(telegram_data)
bot = Bot(token=data["telegram_token"])
client = Dispatcher(bot)
admin_id = [489951151, 857280061]


def analytics(message: types.Message):
    with open('analytics.txt', '+r') as user_id:
        if str(message.from_user.id) not in user_id.read():
            user_id.write(f'{message.from_user.id, message.from_user.username}\n')


@client.message_handler(commands=["start", "help", "хелп", "помощь", "гайд"])
async def manual(msg: types.Message):
    with open("package/client_lock.json", "r") as file:
        sys = load(file)
    await msg.answer(f"""👋Привет, {msg.from_user.first_name}.\n🤖Я - бот {sys['name']}, решающий ЦДЗ.
(Version: {sys['version']})
    \nВК создателя: {sys['vk']}\n
Для начала работы, отправь мне ссылку на тест и я постараюсь найти ответы.\n
Если возникла какая-либо проблема, ошибка, баг обратитесь в чат поддержки👨🏼‍🔧: {sys['help_place']}.
Там Вам помогут с сложившейся ситуацией.🎯""")
    analytics(msg)


@client.message_handler(commands=['admin', 'analytics'])
async def admin(msg: types.Message):
    with open("analytics.txt", "r") as analytic:
        if msg.from_user.id in admin_id:
            counter = 0
            for number, id_user in enumerate(analytic.readlines()):
                await msg.answer(f'{number + 1}. User: {id_user}')
                counter += 1
            await msg.answer(f'🙈Всего пользователей: {counter}')
        else:
            await msg.answer("🤡Для начала, отправь ссылку на тест, и я попробую его решить.")


@client.message_handler(content_types=["text"])
async def get_text_messages(msg: types.Message):
    if msg.text.startswith("http"):
        try:
            start_time = time.time()
            await msg.answer("👽Начал решать...")
            answers = core.get_answers(link=msg.text)
            for task_number, task in enumerate(answers):
                await msg.answer(f"Вопрос №{task_number + 1}: {task[0]}\n\nОтвет: {task[1]}")
            await msg.answer(f"⏳Решено за {'%s секунд' % round((time.time() - start_time), 1)}")
        except:
            await msg.answer('🤔Хм странно, но я ничего не нашел. Проверь правильность ссылки или нажми /help')
    else:
        await msg.answer("😉Для начала, отправь ссылку на тест, и я попробую его решить.🛸")

    info = f'Text: {msg.text}\nUser: {msg.from_user.get_user_profile_photos}'
    await bot.send_message(admin_id[0], info)
    analytics(msg)


if __name__ == "__main__":
    print(f"Connected at {datetime.today().strftime('%H:%M, %d-%m-%Y')}")
    executor.start_polling(client)
