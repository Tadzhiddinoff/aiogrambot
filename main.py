from aiogram import Dispatcher, Bot, types, executor
import os
from app import keyboards as kb
from app import database as db
# python-dotenv предназначен для загрузки переменных среды из файла .env в ваш проект
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    print(122222)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMZZZkTNWGshfvcDGvyEurkrOVmdBgAAnASAAKNbhlIUVJC-YI7dVg0BA')
    await message.answer(f'{message.from_user.first_name} добро пожаловать в магазин кроссовок!',
                         reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как админ!', reply_markup=kb.main_admin)


@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=kb.catalog_list)


@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')


@dp.message_handler(text='Поддержка')
async def support(message: types.Message):
    await message.answer(
        f'Появились какие нибудь вопросы при использовании бота? Tогда обратитесь к администратору: @d_27d')


@dp.message_handler(text='Админ-панель')
async def panel_admin(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer('Вы вошли в панель администратора', reply_markup=kb.admin_panel)
    else:
        await message.reply('Я тебя не понимаю')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
