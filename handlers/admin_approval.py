from telebot import types

def setup(bot):
    @bot.callback_query_handler(func=lambda call: call.data.startswith('approve_') or call.data.startswith('reject_'))
    def handle_admin_decision(call):
        user_id = int(call.data.split('_')[1])
        if 'approve' in call.data:
            bot.send_message(user_id, "\u2705 Your registration has been approved. Welcome!")
            bot.send_message(ADMIN_CHAT_ID, f"User {user_id} has been approved.")
            pending_users.pop(user_id, None)
        elif 'reject' in call.data:
            msg = bot.send_message(ADMIN_CHAT_ID, "Please provide a rejection reason:")
            bot.register_next_step_handler(msg, get_rejection_reason, user_id)

    def get_rejection_reason(message, user_id):
        reason = message.text
        bot.send_message(user_id, f"\u274C Your registration was rejected. Reason: {reason}")
        bot.send_message(ADMIN_CHAT_ID, f"User {user_id} has been rejected. Reason: {reason}")
        pending_users.pop(user_id, None)
