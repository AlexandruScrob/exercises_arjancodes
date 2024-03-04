from colorama import Fore as f
from typing import Callable

Command = tuple[str, list[str]]

SHELL_HEADER = f" {f.YELLOW}[*] {f.CYAN}-> {f.WHITE}"


COMMANDS: dict[str, Callable[[list[str]], None]] = {}


# NOTE: plugin interface
def add_command(command: str, function: Callable[[list[str]], None]) -> None:
    COMMANDS[command] = function


def execute(command: str, arguments: list[str]) -> None:
    if command in COMMANDS and len(arguments) > 0:
        COMMANDS[command](arguments)


def run_shell() -> None:
    while True:
        command, arguments = shell_input()
        execute(command, arguments)


def shell_input() -> Command:
    """Gets User input then returns a parsed command."""
    user_input = input(SHELL_HEADER)
    return parse_command_string(user_input)


def parse_command_string(cmd: str) -> Command:
    """Parses a command and returns the command and its args."""
    command_parts = cmd.split()

    command = command_parts[0].lower().strip()
    arguments = [part.strip() for part in command_parts[1:]]
    return command, arguments
