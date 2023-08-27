import os, logging, time

from aiogram import Bot, executor, Dispatcher, types


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

logging.basicConfig(filename='logfile.log', level=logging.INFO)


async def main(_):
    print('>>> Start bot <<<')


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.answer('Hello')
    await bot.send_message(user_id, f'I\'am gadalka, your name is - {user_name} !')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=main, skip_updates=True)


# New data
