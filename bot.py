import telebot
from telebot import types

# Устанавливаем токен вашего бота
TOKEN = '5846035210:AAG9D2G3fvJyUlUfMSOqE_Wq6cJ6V1Fdit4'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Определяем обработчик для команды /start
@bot.message_handler(commands=['start'])
def start(message):
    #bot.send_message(message.chat.id, 'Привет! Я бот, который показывает последние обновления камеры видеонаблюдения!')
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('Показать камеры')
    markup.row(button)
    bot.send_message(message.chat.id, 'Привет! Я бот, который показывает последние обновления камеры видеонаблюдения!', reply_markup=markup)
    
# Запускаем бота
bot.polling(none_stop=True)
