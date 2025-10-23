import datetime, random, platform

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

def get_system_info():
    return (
        f"🖥️ *System Information*\n\n"
        f"Python version: {platform.python_version()}\n"
        f"System: {platform.system()}\n"
        f"Machine: {platform.machine()}\n"
        f"Node: {platform.node()}"
    )
