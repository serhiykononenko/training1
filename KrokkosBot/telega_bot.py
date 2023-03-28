import config
import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot(config.TOKEN_BOT)


@bot.message_handler(commands=['start', 'hello', 'main', 'привет', 'hi'])
def main(message):
    f_name = message.from_user.first_name
    l_name = message.from_user.last_name if message.from_user.last_name is not None else ''
    bot.send_message(message.chat.id, f'Hello, {f_name} {l_name}!')


@bot.message_handler(commands=['site', 'website'])
def go_to_site(message):
    webbrowser.open('https://www.gismeteo.ua/weather-kyiv-4944/#tab_0')


@bot.message_handler(content_types=['photo'])
def det_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Weather in Kyiv', url='https://www.gismeteo.ua/weather-kyiv-4944/#tab_0')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete picture', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Cool picture!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information!</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if 'hello' in message.text.lower():
        bot.send_message(message.chat.id, f'Hello, {f_name_l_name(message)}!')
    elif 'id' in message.text.lower():
        bot.reply_to(message, f'ID: {message.from_user.id}')


def f_name_l_name(message) -> str:
    f_name = message.from_user.first_name
    l_name = message.from_user.last_name if message.from_user.last_name is not None else ''
    return f'{f_name} {l_name}'

# bot.polling(none_stop=True)
bot.infinity_polling()

# import requests
# import telegram
# from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
#
# API_KEY = "ваш API-ключ от OpenWeatherMap"
# bot = telegram.Bot("ваш токен бота Telegram")
#
# def start(update, context):
#     context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я бот для получения погоды. Введите название города, чтобы получить погоду.")
#
# def get_weather(update, context):
#     city_name = update.message.text
#     api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
#     response = requests.get(api_url)
#     data = response.json()
#     if data["cod"] == 200:
#         weather_description = data["weather"][0]["description"]
#         temperature = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         humidity = data["main"]["humidity"]
#         wind_speed = data["wind"]["speed"]
#         message_text = f"Погода в городе {city_name}: {weather_description}\nТемпература: {temperature}°C\nОщущается как: {feels_like}°C\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с"
#         context.bot.send_message(chat_id=update.message.chat_id, text=message_text)
#     else:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Не удалось получить погоду для данного города.")
#
# def main():
#     updater = Updater("ваш токен бота Telegram")
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_weather))
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
#
#
#
