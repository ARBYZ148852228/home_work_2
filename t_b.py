import telebot

# Ваш токен API от BotFather
API_TOKEN = '7871780176:AAFUvU68Z-Oj1zwq-bOtsOMWdBC9NjKd99E'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "Привет! И тебе всего хорошего!!!")

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling(none_stop=True)