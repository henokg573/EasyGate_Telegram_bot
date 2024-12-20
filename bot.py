import os
from telebot import TeleBot
from handlers import start_handler, button_handler, user_registration, admin_approval
from config import TOKEN

bot = TeleBot(TOKEN)

# Initialize all handlers
start_handler.setup(bot)
button_handler.setup(bot)
user_registration.setup(bot)
admin_approval.setup(bot)

if __name__ == '__main__':
    print("Bot is running...")
    bot.polling(non_stop=True, timeout=60)
