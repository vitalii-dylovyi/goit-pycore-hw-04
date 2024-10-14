import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_contents(directory, prefix=""):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return

    items = list(directory.iterdir())
    items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        current_prefix = "└── " if is_last else "├── "

        if item.is_dir():
            print(f"{prefix}{current_prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_contents(item, next_prefix)
        else:
            print(f"{prefix}{current_prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task_3.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        print(f"Directory structure of {directory_path}:")
        print_directory_contents(directory_path)
