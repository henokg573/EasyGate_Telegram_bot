from telebot import types
from utils.file_utils import validate_file

pending_users = {}

def setup(bot):
    # Step 1: Ask Full Name
    @bot.message_handler(func=lambda message: message.text == 'Continue')
    def ask_full_name(message):
        msg = bot.reply_to(message, "Please enter your full name:")
        bot.register_next_step_handler(msg, get_full_name)

    # Step 2: Validate and store user data
    def get_full_name(message):
        full_name = message.text.strip()
        if not full_name.isalpha() or len(full_name) <= 3:
            msg = bot.reply_to(message, "Invalid name. Please enter a valid full name (only alphabets, at least 4 characters):")
            bot.register_next_step_handler(msg, get_full_name)
            return
        user_id = message.from_user.id
        pending_users[user_id] = {'full_name': full_name}
        msg = bot.reply_to(message, "Enter your email address:")
        bot.register_next_step_handler(msg, get_email)

    def get_email(message):
        email = message.text.strip()
        if not email.endswith("@gmail.com"):
            msg = bot.reply_to(message, "Invalid email. Please enter a valid Gmail address:")
            bot.register_next_step_handler(msg, get_email)
            return
        user_id = message.from_user.id
        pending_users[user_id]['email'] = email
        msg = bot.reply_to(message, "Enter your phone number:")
        bot.register_next_step_handler(msg, get_phone_number)

    def get_phone_number(message):
        phone_number = message.text.strip()
        if not phone_number.isdigit() or len(phone_number) != 10:
            msg = bot.reply_to(message, "Invalid phone number. Please enter a 10-digit phone number:")
            bot.register_next_step_handler(msg, get_phone_number)
            return
        user_id = message.from_user.id
        pending_users[user_id]['phone_number'] = phone_number
        msg = bot.reply_to(message, "Upload a file for verification (PDF or image, Max: 10MB):")
        bot.register_next_step_handler(msg, get_verification_file)

    def get_verification_file(message):
        user_id = message.from_user.id
        if message.content_type == 'document':
            if not validate_file(message.document):
                msg = bot.reply_to(message, "Invalid file type or size. Please upload a PDF or image file below 10MB.")
                bot.register_next_step_handler(msg, get_verification_file)
                return
            pending_users[user_id]['file_id'] = message.document.file_id
            ask_payment_proof(message)
        else:
            msg = bot.reply_to(message, "Please upload a valid document file (PDF or image):")
            bot.register_next_step_handler(msg, get_verification_file)
