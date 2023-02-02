# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot_commands import *
from config import token

def main() -> None:
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("hello", hello_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CallbackQueryHandler(button))




    print("Start server")
    app.run_polling()


if __name__ == "__main__":
    main()