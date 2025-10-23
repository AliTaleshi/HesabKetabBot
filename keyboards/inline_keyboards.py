from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📅 Current Date", callback_data="date"),
            InlineKeyboardButton("⏰ Current Time", callback_data="time")
        ],
        [
            InlineKeyboardButton("🔤 Random Joke", callback_data="joke"),
            InlineKeyboardButton("📊 System Info", callback_data="system")
        ],
        [
            InlineKeyboardButton("❓ Help", callback_data="help")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def settings_menu_keyboard():
    settings_keyboard = [
            [
                InlineKeyboardButton("Hide Keyboard", callback_data="hide_keyboard"),
                InlineKeyboardButton("Show Keyboard", callback_data="show_keyboard")
            ],
            [
                InlineKeyboardButton("Theme: Light", callback_data="theme_light"),
                InlineKeyboardButton("Theme: Dark", callback_data="theme_dark")
            ]
        ]
    return InlineKeyboardMarkup(settings_keyboard)

def return_to_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Return to Menu", callback_data="menu")]]
    return InlineKeyboardMarkup(keyboard)
