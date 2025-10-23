from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline_keyboards import main_menu_keyboard
from keyboards.reply_keyboards import main_reply_keyboard, remove_keyboard

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message and display main menu and quick access keyboard."""
    user = update.effective_user

    await update.message.reply_text(
        f"Hello {user.first_name}! I'm your interactive Telegram bot.\n"
        "Please select an option from the menu below or use the quick access buttons at the bottom of your chat!",
        reply_markup=main_menu_keyboard()
    )
    await update.message.reply_text(
        "Quick access buttons are now available at the bottom of your chat!",
        reply_markup=main_reply_keyboard()
    )


# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help information."""
    help_text = (
        "🤖 *Bot Commands* 🤖\n\n"
        "/start - Display the main menu and quick access keyboard\n"
        "/help - Show this help message\n"
        "/menu - Show the main menu again\n"
        "/keyboard - Show the quick access keyboard\n"
        "/hidekeyboard - Hide the quick access keyboard\n\n"
        "You can also interact with the buttons and reply keyboard!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


# /menu command
async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the main inline button menu."""
    await update.message.reply_text(
        "Main Menu - Please select an option:",
        reply_markup=main_menu_keyboard()
    )


# /keyboard command
async def show_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the reply (bottom) keyboard."""
    await update.message.reply_text(
        "Quick access buttons restored!",
        reply_markup=main_reply_keyboard()
    )


# /hidekeyboard command
async def remove_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hide the reply keyboard."""
    await update.message.reply_text(
        "Keyboard removed. Type /keyboard to show it again.",
        reply_markup=remove_keyboard()
    )
