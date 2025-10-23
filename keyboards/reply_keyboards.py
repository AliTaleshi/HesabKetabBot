from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def main_reply_keyboard():
    keyboard = [
        ["🏠 Home", "❓ Help"],
        ["📅 Today", "📝 Notes"],
        ["🔍 Search", "⚙️ Settings"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

def remove_keyboard():
    return ReplyKeyboardRemove()
