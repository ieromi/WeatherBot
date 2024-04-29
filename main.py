from aiogram import Bot, types, Dispatcher, executor
from weather import weather_report
from datetime import datetime
import asyncio

bot = Bot(token='token')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def say_hi(message: types.Message):
    await message.reply(f"Привет!\nЯ - погодный бот для Москвы!\nБ"
                        f"уду отправлять тебе прогноз погоды ежедневно в 08:30.\n"
                        f"Для вызова прогноза на ближайшее время набери команду /forecast .")


@dp.message_handler(commands=['auto'])
async def command_start(message: types.Message):
    while True:
        await asyncio.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == '08:30:00':
            await message.answer(f"Доброе утро!\nПрогноз погоды на сегодня:\n\n{weather_report()}")


@dp.message_handler(commands=['forecast'])
async def make_forecast(message: types.Message):
    await message.answer(f"Прогноз погоды на ближайшее время:\n\n{weather_report()}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
