import telebot
from telebot import types
from datetime import datetime
import random

API_TOKEN = '7135763386:AAEbW9ba5zHzTO4m7V4GqZGo4dA-noHz--Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Узнать время")
    button2 = types.KeyboardButton("Рандомное число")
    button3 = types.KeyboardButton("Мой ID")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Узнать время":
        current_time = datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.chat.id, f"Текущее время в Москве: {current_time}")
    elif message.text == "Рандомное число":
        random_number = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Случайное число: {random_number}")
    elif message.text == "Мой ID":
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
    else:
        bot.send_message(message.chat.id, "Неизвестная команда. Пожалуйста, выберите из меню.")

bot.polling(none_stop=True)