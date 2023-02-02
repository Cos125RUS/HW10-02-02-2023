from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from spy import *
from weather import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.chat.id # id пользователя
    update.effective_user.first_name # first_name пользователя на входе
    update.message.chat.first_name # first_name пользователя на выходе
    # <class 'telegram._update.Update'>
    log(update, context)
    # user_id = update.effective_user.id 
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/weather <<City>>\nFor example:\n/weather Moscow')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    alpha = "АБВГДЕЖЗИК"
    keyboard = [[InlineKeyboardButton("Владивосток", callback_data="Владивосток"), 
        InlineKeyboardButton("Томск", callback_data="Томск")],  
        [InlineKeyboardButton("Хабаровск", callback_data="Хабаровск "), 
        InlineKeyboardButton("Новосибирск", callback_data="Новосибирск")],
        [InlineKeyboardButton("Краснодар", callback_data="Краснодар"), 
        InlineKeyboardButton("Екатеринбург", callback_data="Екатеринбург")], 
        [InlineKeyboardButton("Москва", callback_data="Москва"), 
        InlineKeyboardButton("Санкт-Петербург", callback_data="Санкт-Петербург")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите город:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    print(query.data) # Нажатая кнопка
    await query.answer(query.data)
    await query.edit_message_text(text=f"{query.data}: weather") # Ответ пользователю


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    # print(update.message.text.replace('/weather ',''))
    cityName = update.message.text.replace('/weather ','')
    weather = get_weather_by_city(f"{cityName}")
    temp = weather['main']['temp']
    windSpeed = weather['wind']['speed']
    cloudiness = weather['weather'][0]['main']
    answer = f'Temp = {temp}\nWind speed = {windSpeed}\nCloudiness = {cloudiness}'
    await update.message.reply_text(answer)


