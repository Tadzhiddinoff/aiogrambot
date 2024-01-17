from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Поддержка')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Поддержка').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Фуболки', url='https://youtube.com/@dalertadzhiddinoff935'),
                 InlineKeyboardButton(text='Джинсы', url='https://youtube.com/@dalertadzhiddinoff935'),
                 InlineKeyboardButton(text='Кроссовки', url='https://youtube.com/@dalertadzhiddinoff935'))
