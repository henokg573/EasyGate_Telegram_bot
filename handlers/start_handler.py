from telebot import types

def setup(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn_about = types.KeyboardButton('About Us')
        btn_services = types.KeyboardButton('Our Services')
        btn_feedback = types.KeyboardButton('Feedback')
        btn_continue = types.KeyboardButton('Continue')
        markup.add(btn_about, btn_services, btn_feedback, btn_continue)
        bot.reply_to(message, "Welcome! Please choose an option:", reply_markup=markup)
