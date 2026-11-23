import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
STYLES = {
    "user": ("🧑 Você", "\033[36m"),       # ciano
    "assistant": ("🤖 Claude", "\033[35m"),  # magenta
}

def print_chat(messages, width=80):
    print(f"\n{BOLD}{'═' * width}{RESET}")
    print(f"{BOLD}{'💬 CONVERSA'.center(width)}{RESET}")
    print(f"{BOLD}{'═' * width}{RESET}")

    for i, msg in enumerate(messages, start=1):
        label, color = STYLES[msg["role"]]
        print(f"\n{color}{BOLD}┌─ {label} {DIM}#{i}{RESET}")
        for line in textwrap.wrap(msg["content"], width=width - 4) or [""]:
            print(f"{color}│{RESET} {line}")
        print(f"{color}└{'─' * (width - 1)}{RESET}")

    print(f"\n{DIM}{len(messages)} mensagens no histórico{RESET}\n")
