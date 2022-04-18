from aiogram import Bot
import asyncio

bot = Bot(token='1565468280:AAFjXX1E3NmAknKqlZP6AoSJWJwMY4aoPJA')
text = ''


async def post():
    with open("analytics.txt", "r") as analytic:
        for id_user in analytic.readlines():
            await bot.send_message(id_user, text)


loop = asyncio.get_event_loop()
loop.run_until_complete(post())
