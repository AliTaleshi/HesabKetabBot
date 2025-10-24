import datetime, random, platform
import re

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't programmers like nature? It has too many bugs."
    ]
    return random.choice(jokes)

def _escape_markdown_v2(text: str) -> str:
    # Escape characters that MarkdownV2 treats as special per Telegram docs
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)

def get_system_info():
    raw = (
        "System Information\n\n"
        f"Python version: {platform.python_version()}\n"
        f"System: {platform.system()}\n"
        f"Machine: {platform.machine()}\n"
        f"Node: {platform.node()}"
    )
    return _escape_markdown_v2(raw)
    