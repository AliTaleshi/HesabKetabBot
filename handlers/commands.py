from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline_keyboards import main_menu_keyboard
from keyboards.reply_keyboards import main_reply_keyboard, remove_keyboard
from services.user_service import get_user_by_telegram_id, register_user
from utils.logger import logger

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Check if user exists
    existing_user = await get_user_by_telegram_id(user.id)

    if not existing_user:
        await register_user(
            telegram_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )
        logger.info(f"Registered new user: {user.id} - {user.username}")
        welcome_message = f"👋 Welcome, {user.first_name}! You have been registered successfully."
    else:
        welcome_message = f"👋 Welcome back, {user.first_name}!"


    await update.message.reply_text(welcome_message, reply_markup=main_menu_keyboard())

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
