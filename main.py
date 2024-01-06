from aiogram import Dispatcher, Bot, types, executor
import os
from aiogram.types import ReplyKeyboardMarkup
# python-dotenv предназначен для загрузки переменных среды из файла .env в ваш проект
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Поддержка')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Поддержка').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMZZZkTNWGshfvcDGvyEurkrOVmdBgAAnASAAKNbhlIUVJC-YI7dVg0BA')
    await message.answer(f'{message.from_user.first_name} добро пожаловать в магазин кроссовок!',
                         reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как админ!', reply_markup=main_admin)


@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!')


@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')


@dp.message_handler(text='Поддержка')
async def support(message: types.Message):
    await message.answer(
        f'Появились какие нибудь вопросы при использовании бота? тогда обратитесь к администратору: @d_27d')


@dp.message_handler(text='Админ-панель')
async def panel_admin(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer('Вы вошли в панель администратора', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp)
