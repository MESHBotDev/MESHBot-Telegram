from aiogram import Bot
import asyncio

bot = Bot(token='1565468280:AAFjXX1E3NmAknKqlZP6AoSJWJwMY4aoPJA')


async def main():
    await bot.send_message(857280061, 'я подсяду?')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
