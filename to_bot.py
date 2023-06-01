from aiogram import Bot, Dispatcher, executor, types
from markups import markups
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from programs.take_last_files import my_path
from programs.parse_program import pob_info_to as parse


API_TOKEN = 'Your API'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def commad_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот підключенний!👋', reply_markup=markups.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🚀START🚀':
        await bot.send_message(message.from_user.id, 'Парсінг почато!💻\nЦе 💩 може зайняти пару хвилин🤷‍♂️')
        await bot.send_message(message.from_user.id, '💯✅ ',
                               reply_markup=parse())
        document = types.input_file.InputFile(f'data/{my_path()}',
                                              filename=f'{my_path()}')
        await bot.send_document(message.from_user.id, document=document, reply_markup=markups.mainMenu)

    elif message.text == 'Site🦠':
        button = InlineKeyboardButton(text="Перейти на сайт",
                                      url="https://tabelaofert.pl/nowe-mieszkania?inwestycja_3d=1")
        markup = InlineKeyboardMarkup().add(button)
        await bot.send_message(message.chat.id, "🧬Натисніть на кнопку, щоб перейти на сайт🧬", reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
