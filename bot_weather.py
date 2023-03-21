from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from time_change import utc_to_local_time as utl
from weather import weather_cheсk

TOKEN = "Token"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    start_msg = (f'Привет, {message.from_user.first_name}!✌️'
                 f'\nЭтот бот работает только с мобильного телефона!📱'
                 f'\nТеперь просто нажми кнопку внизу экрана и получишь '
                 f'погоду!📍')
    kb = get_keyboard()
    await message.answer(start_msg, reply_markup=kb)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Узнать погоду", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    weather = weather_cheсk(lat, lon)
    main = weather['weather'][0]['description']
    temp = weather['main']['temp']
    temp_felt = weather['main']['feels_like']
    humidity = weather['main']['humidity']
    visibility = weather['visibility']
    if visibility > 1000:
        visibility = f'{str(visibility)[:-3]} к'
    sunrise = utl(weather['sys']['sunrise'])
    sunset = utl(weather['sys']['sunset'])
    kb = get_keyboard()
    reply = (f'Погода в твоем местоположение📍:'
             f'\nСейчас {main}'
             f'\n🌡️Температура {temp}°C, ощущается как {temp_felt}°C'
             f'\n🌤Влажность {humidity}%'
             f'\n🏙️Видимость {visibility}м'
             f'\n🌅Восход солна {sunrise}'
             f'\n🌇Закат солнца {sunset}')

    await message.answer(reply, reply_markup=kb)




@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f'Я тебя не понимаю!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
