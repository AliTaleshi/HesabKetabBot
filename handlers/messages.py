from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from keyboards.inline_keyboards import main_menu_keyboard, settings_menu_keyboard, return_to_menu_keyboard
from keyboards.reply_keyboards import main_reply_keyboard, remove_keyboard
from utils.helpers import get_current_date

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user text messages and reply keyboard button presses."""
    text = update.message.text

    if text == "🏠 Home":
        await update.message.reply_text("Main Menu - Please select an option:", reply_markup=main_menu_keyboard())
        return

    elif text == "❓ Help":
        help_text = (
            "🤖 *Bot Commands* 🤖\n\n"
            "/start - Display main menu\n"
            "/help - Show help\n"
            "/menu - Show menu again\n"
            "/keyboard - Show keyboard\n"
            "/hidekeyboard - Hide keyboard"
        )
        await update.message.reply_text(help_text, parse_mode="Markdown")
        return

    elif text == "📅 Today":
        await update.message.reply_text(f"📅 Today's date is: {get_current_date()}")
        return

    elif text == "📝 Notes":
        await update.message.reply_text(
            "📝 Your Notes\n\n"
            "You don't have any notes yet. You can create notes using the /note command followed by your note content."
        )
        return

    elif text == "🔍 Search":
        await update.message.reply_text("🔍 Type your search query after /search command.")
        return

    elif text == "⚙️ Settings":
        await update.message.reply_text("⚙️ Settings:", reply_markup=settings_menu_keyboard)
        return

    await update.message.reply_text(
        f"You said: {text}\n\nNeed anything else?",
        reply_markup=return_to_menu_keyboard
    )
