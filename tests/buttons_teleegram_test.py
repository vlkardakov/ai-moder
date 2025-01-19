import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инициализация бота
TOKEN = '7923293677:AAH9l0wC1StMncKbrY1yuVpgP65JR80LWVw'
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения состояния кнопок для каждого пользователя
user_button_states = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Инициализируем состояния кнопок для пользователя
    user_button_states[message.chat.id] = {
        "button1": False,
        "button2": False
    }

    # Отправляем сообщение с кнопками
    bot.send_message(
        message.chat.id,
        "Выберите кнопку:",
        reply_markup=generate_keyboard(message.chat.id)
    )


# Генерация клавиатуры с учетом состояния кнопок
def generate_keyboard(chat_id):
    # Получаем состояния кнопок для пользователя
    states = user_button_states.get(chat_id, {})

    # Создаем Inline-клавиатуру
    keyboard = InlineKeyboardMarkup()
    button1_text = "✅ Разбанить ✅" if states.get("button1") else "❌ Забанить ❌"
    button2_text = "✅ Разбанить по редиректу ✅" if states.get("button2") else "❌ Забанить по редиректу ❌"
    button1 = InlineKeyboardButton(button1_text, callback_data="button1")
    button2 = InlineKeyboardButton(button2_text, callback_data="button2")
    keyboard.add(button1, button2)
    return keyboard


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id

    # Обновляем состояние кнопки
    if call.data == "button1":
        user_button_states[chat_id]["button1"] = not user_button_states[chat_id]["button1"]
    elif call.data == "button2":
        user_button_states[chat_id]["button2"] = not user_button_states[chat_id]["button2"]

    # Обновляем клавиатуру без изменения текста сообщения
    bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=call.message.message_id,
        reply_markup=generate_keyboard(chat_id)
    )


# Запуск бота
bot.polling()
