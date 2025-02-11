import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram import Application

API_TOKEN = '8031754163:AAHcga51N1WGI7ArBJUBO7_waBHCuQTLKzc'



quotes = [
    "Веруй в себя и ты уже на полпути к успеху.",
    "Ваши ограничения — это только ваше воображение.",
    "Толкайте себя, потому что никто другой этого не сделает.",
    "Великие вещи никогда не происходят в зоне комфорта.",
    "Мечтайте об этом. Желайте этого. Делайте это."
]

@app.command()
async def start(update: types.Update):
    await update.message.reply("Добро пожаловать! Используйте команду /motivate, чтобы получить вашу порцию мотивации!")

@app.command()
async def motivate(update: types.Update):
    quote = random.choice(quotes)
    await update.message.reply(quote)

async def main():
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())

