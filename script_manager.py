import telebot  # импорт телебота
from telebot import types  # импорт клавиатур
import os
import subprocess  # подключаем взаимодействие с файлами

bot = telebot.TeleBot('1889117929:AAHBIYnaOAx4a-gqz9D2ooKwAf-3gVigvU0')


@bot.message_handler(commands=['start'])
def start(message):
    project_board = types.InlineKeyboardMarkup()
    aviso_button = types.InlineKeyboardButton(text='Aviso', callback_data='aviso')
    project_board.add(aviso_button)
    bot.send_message(message.chat.id, 'Привет. Начнем работу. Какой проект запускаем?', reply_markup=project_board)


@bot.message_handler(commands=['kill'])
def start(message):
    project_board = types.InlineKeyboardMarkup()
    aviso_button = types.InlineKeyboardButton(text='Aviso', callback_data='aviso_kill')
    project_board.add(aviso_button)
    bot.send_message(message.chat.id, 'Какой процесс остановить?', reply_markup=project_board)


@bot.callback_query_handler(func=lambda callback: callback.data)
def run_aviso(callback):
    if callback.data == 'aviso':
        bot.send_message(770675831, 'Запускаю проект Aviso')
        subprocess.run("aviso_telegram.exe", shell=True)
    elif callback.data == 'aviso_kill':
        bot.send_message(770675831, 'Останавливаю проект Aviso')
        subprocess.Popen.terminate('aviso_telegram.exe')  # to do


bot.polling()
