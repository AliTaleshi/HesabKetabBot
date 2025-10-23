from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config.config import BOT_TOKEN
from handlers import commands, messages, callbacks
from utils.logger import logger

def main():
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

    logger.info("Bot started")
    application.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
