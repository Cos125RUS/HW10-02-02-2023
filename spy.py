from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def log(update: Update, context: ContextTypes):
    with open('dataLog.csv', 'a', encoding='utf-8') as file:
        file.write(f'time={datetime.datetime.now()}, user_name={update.effective_user.first_name}, id={update.effective_user.id}, command={update.message.text}\n')