def setup(bot):
    @bot.message_handler(func=lambda message: message.text in ['About Us', 'Our Services', 'Feedback', 'Continue'])
    def handle_buttons(message):
        if message.text == 'About Us':
            bot.reply_to(message, "We are a company that provides various services.")
        elif message.text == 'Our Services':
            bot.reply_to(message, "We offer a range of services including A, B, and C.")
        elif message.text == 'Feedback':
            bot.reply_to(message, "Please provide your feedback.")
        elif message.text == 'Continue':
            ask_full_name(message)
