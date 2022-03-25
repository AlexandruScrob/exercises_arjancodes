"""
Example application showing Python 3.10 structural pattern matching.
"""


from dataclasses import dataclass
from typing import List
import shlex


def run_command(command: str) -> None:
    match command:
        case "quit":
            print("Quitting the program.")
            quit()

        case "reset":
            print("Resetting the system")

        case other:
            print(f"Uknown command: {other!r}.")


def run_command_v2(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading file: {filename}.")
        case ["save", filename]:
            print(f"Saving to file: {filename}.")
        case ["quit" | "exit" | "bye", *rest]:
            if "--force" in rest or "-f" in rest:
                print("Sending SIGTERM to all processes and quitting the program.")
            else:
                print("Quitting the program.")
            quit()
        case _:
            print(f"Uknown command: {command!r}.")


def run_command_v3(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading file: {filename}.")
        case ["save", filename]:
            print(f"Saving to file: {filename}.")
        case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case ["quit" | "exit" | "bye", *rest]:
            print("Quitting the program.")
            quit()
        case _:
            print(f"Uknown command: {command!r}.")


@dataclass
class Command:
    """Class that represents a command."""

    command: str
    arguments: List[str]


# Downsides include:
#   - cases run from top to bottom
#   - order matters -> loosing cohesion
def run_command_v4(command: Command) -> None:
    match command:
        case Command(command="load", arguments=[filename]):
            print(f"Loading file: {filename}.")
        case Command(command="save", arguments=[filename]):
            print(f"Saving to file: {filename}.")
        case Command(
            command="quit" | "exit" | "bye", arguments=["--force" | "-f", *rest]
        ):
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case Command(command="quit" | "exit" | "bye"):
            print("Quitting the program.")
            quit()
        case _:
            print(f"Uknown command: {command!r}.")


def main() -> None:
    """Main function."""

    while True:
        command, *arguments = shlex.split(input("$ "))

        run_command_v4(Command(command, arguments))


if __name__ == "__main__":
    main()
