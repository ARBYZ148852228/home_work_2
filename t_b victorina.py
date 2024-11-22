import random
from telebot import TeleBot

# Токен вашего бота
TOKEN = '7871780176:AAFUvU68Z-Oj1zwq-bOtsOMWdBC9NjKd99E'


# Создаем экземпляр бота
bot = TeleBot(TOKEN)

# Вопросы и ответы для разных уровней сложности
questions = {
    # Уровень 1 (Легкий)
    1: [
        {"question": "Какой океан является самым большим?", "answer": "Тихий"},
        {"question": "Какая река самая длинная в мире?", "answer": "Нил"},
        {"question": "Столица Франции?", "answer": "Париж"}
    ],
    # Уровень 2 (Средний)
    2: [
        {"question": "В каком городе находится Эйфелева башня?", "answer": "Париж"},
        {"question": "Какое море омывает берега Турции?", "answer": "Черное"},
        {"question": "Самая высокая гора в мире?", "answer": "Эверест"}
    ],
    # Уровень 3 (Сложный)
    3: [
        {"question": "Какое самое глубокое озеро в мире?", "answer": "Байкал"},
        {"question": "Как называется столица Новой Зеландии?", "answer": "Веллингтон"},
        {"question": "Какое государство занимает самый большой остров в мире?", "answer": "Гренландия"}
    ]
}

# Функция для выбора случайного вопроса
def get_random_question(level):
    return random.choice(questions[level])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}! Давай начнем викторину по географии.')
    bot.send_message(message.chat.id, 'Выбери уровень сложности:\n1. Легкий\n2. Средний\n3. Сложный')

# Обработчик команд уровня сложности
@bot.message_handler(func=lambda message: message.text in ['1', '2', '3'])
def select_level(message):
    level = int(message.text)
    question = get_random_question(level)
    bot.send_message(message.chat.id, f"Вопрос: {question['question']}")
    bot.register_next_step_handler(message, lambda msg: check_answer(msg, question["answer"], level))

# Проверка ответа
def check_answer(message, correct_answer, level):
    if message.text.lower() == correct_answer.lower():
        bot.send_message(message.chat.id, "Правильно!")
        next_question(message, level)
    else:
        bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {correct_answer}.")
        next_question(message, level)

# Следующий вопрос
def next_question(message, level):
    question = get_random_question(level)
    bot.send_message(message.chat.id, f"Вопрос: {question['question']}")
    bot.register_next_step_handler(message, lambda msg: check_answer(msg, question["answer"], level))

if __name__ == '__main__':
    bot.polling()