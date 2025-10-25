from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config.config import BOT_TOKEN, DATABASE_URL
from handlers import commands, messages, callbacks
from utils.logger import logger
from database.init_db import init_models
from database.db import init_engine

# --- Initialize DB (engine only) synchronously ---
init_engine(DATABASE_URL)

# PTB Application
application = Application.builder().token(BOT_TOKEN).build()

# Command handlers
application.add_handler(CommandHandler("start", commands.start))
application.add_handler(CommandHandler("help", commands.help_command))
application.add_handler(CommandHandler("menu", commands.menu_command))
application.add_handler(CommandHandler("keyboard", commands.show_keyboard))
application.add_handler(CommandHandler("hidekeyboard", commands.remove_keyboard))

# Message handler
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages.echo))

# Callback query handler
application.add_handler(CallbackQueryHandler(callbacks.button_callback))

# --- Async DB init inside PTB loop ---
async def async_init(app):
    await init_models()
    logger.info("✅ Database initialized successfully.")

application.post_init = async_init

if __name__ == "__main__":
    logger.info("🚀 Starting bot...")
    # PTB will handle the asyncio loop itself
    application.run_polling()
