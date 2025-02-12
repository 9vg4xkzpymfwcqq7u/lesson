import logging
import random
import string
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '8031754163:AAHcga51N1WGI7ArBJUBO7_waBHCuQTLKzc'


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Добро пожаловать в бот-генератор паролей! Используйте команду /generate для получения пароля.")
    logger.info(f"User {message.from_user.username} started the bot.")

@dp.message_handler(commands=['generate'])
async def cmd_generate(message: types.Message):
    password = generate_password()
    await message.reply(f"Ваш новый пароль: {password}")
    logger.info(f"User {message.from_user.username} generated a password: {password}")

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.reply("Команды:\n/start - начать\n/generate - сгенерировать пароль\n/help - помощь")
    logger.info(f"User {message.from_user.username} requested help.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

