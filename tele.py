import random
import string
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '8031754163:AAHcga51N1WGI7ArBJUBO7_waBHCuQTLKzc'  # Замените на токен вашего бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши /generate, чтобы сгенерировать случайный пароль.")

@dp.message_handler(commands=['generate'])
async def send_password(message: types.Message):
    password = generate_password()
    await message.reply(f"Сгенерированный пароль: {password}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



