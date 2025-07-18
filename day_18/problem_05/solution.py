chat_log = []

def log_message(user, message):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    chat_log.append(f"{timestamp} - {user}: {message}")

log_message("Aryan", "Hello, team!")
log_message("GPT", "Let's deploy this on Azure!")
print("\n".join(chat_log))
