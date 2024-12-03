def split_message(text, max_length=4096):
    """Splits the message into parts, if it exceeds Telegram's allowed length."""
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def trim_line(line):
    """Extracts the name of an item from a string."""
    try:
        return line.split(" x ")[1].split("for")[0].strip()
    except IndexError:
        return line
