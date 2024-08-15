from aiogram import types


btns = [
		[
		types.KeyboardButton(text="Список концертов"),
		types.KeyboardButton(text="Добавить концерт"),
		]
	]
start_keyboard = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)


btns = [
		[
		types.KeyboardButton(text="Вариант 1"),
		types.KeyboardButton(text="Вариант 2")
		]
	]
variants_keyboard = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)