import telebot
import time
import os

TOKEN = '7923293677:AAH9l0wC1StMncKbrY1yuVpgP65JR80LWVw'
bot = telebot.TeleBot(TOKEN)

print("imported")

def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)  # Используем локальный словарь для хранения переменных
        return local_vars.get('result')  # Возвращаем значение переменной result




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Что нада?")

if __name__ == "__main__":
    bot.polling()