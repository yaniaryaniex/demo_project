# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SkillMap
import sys

ANSI = sys.stdout.isatty()

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

def colorize(text, color):
    if ANSI:
        return f"{color}{text}{Colors.RESET}"
    return text

def bold(text):
    if ANSI:
        return f"{Colors.BOLD}{text}{Colors.RESET}"
    return text

def dim(text):
    if ANSI:
        return f"{Colors.DIM}{text}{Colors.RESET}"
    return text

def underline(text):
    if ANSI:
        return f"{Colors.UNDERLINE}{text}{Colors.RESET}"
    return text

def reverse(text):
    if ANSI:
        return f"{Colors.REVERSE}{text}{Colors.RESET}"
    return text

def hidden(text):
    if ANSI:
        return f"{Colors.HIDDEN}{text}{Colors.RESET}"
    return text

def bg(text, bg_color):
    if ANSI:
        return f"{bg_color}{Colors.RESET}{Colors.BLACK}{text}{Colors.RESET}"
    return text
