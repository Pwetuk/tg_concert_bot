from config import *

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
import key_board_markups as kbm

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN) 
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
	await message.answer("Hello", reply_markup=kbm.start_keyboard)


@dp.message(Command("test"))
async def cmd_test(message: types.Message):
	await message.answer("Тест", reply_markup=kbm.variants_keyboard)

@dp.message(Command('remove'))
async def cmd_remove(message: types.Message):
	await message.answer("Убрано", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == "Список концертов")
async def reply(message: types.Message):
	with open("data.txt", 'r') as f:
		await message.answer(f.readline())



async def main():
	await dp.start_polling(bot)
