from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from keyboards.inline_keyboards import main_menu_keyboard
from keyboards.reply_keyboards import main_reply_keyboard
from utils.helpers import get_current_date, get_current_time, get_random_joke, get_system_info

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses."""
    query = update.callback_query
    await query.answer()  # Removes the Telegram loading spinner

    callback_data = query.data

    # Handle each button action
    if callback_data == "date":
        await query.message.reply_text(f"📅 Today's date is: {get_current_date()}")

    elif callback_data == "time":
        await query.message.reply_text(f"⏰ Current time is: {get_current_time()}")

    elif callback_data == "joke":
        await query.message.reply_text(f"😄 {get_random_joke()}")

    elif callback_data == "system":
        await query.message.reply_text(get_system_info(), parse_mode="Markdown")

    elif callback_data == "help":
        help_text = (
            "🤖 *Bot Commands* 🤖\n\n"
            "/start - Display the main menu and quick access keyboard\n"
            "/help - Show this help message\n"
            "/menu - Show the main menu again\n"
            "/keyboard - Show the quick access keyboard\n"
            "/hidekeyboard - Hide the quick access keyboard\n\n"
            "You can also interact with the buttons on the menu and keyboard!"
        )
        await query.message.reply_text(help_text, parse_mode="Markdown")

    elif callback_data == "menu":
        await query.message.reply_text("Main Menu - Please select an option:", reply_markup=main_menu_keyboard())

    elif callback_data == "hide_keyboard":
        await query.message.reply_text(
            "Keyboard hidden. Type /keyboard to show it again.",
            reply_markup=ReplyKeyboardRemove()
        )

    elif callback_data == "show_keyboard":
        await query.message.reply_text(
            "Quick access buttons restored!",
            reply_markup=main_reply_keyboard()
        )

    elif callback_data.startswith("theme_"):
        theme = callback_data.split("_")[1]
        await query.message.reply_text(
            f"Theme set to {theme.capitalize()}. (Demo — actual theme change would require client-side implementation)"
        )
