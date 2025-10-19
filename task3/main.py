import sys
from pathlib import Path
from colorama import Fore, Style

def help():
    return """
Example:
main.py path/to/a/directory    
"""

if (len(sys.argv) == 1):
    print("No arguments specified")
    print(help())
    exit(1)

folder = Path(sys.argv[1])

if not folder.exists():
    print(f"Error: a directory '{folder}' doesn't exist.")
    exit(2)
elif folder.is_file():
    print(f"Warn: '{folder}' is a file, not a directory. You should pass a directory.")
    exit(3)

def print_folder(name, level):
    print(f"{Style.RESET_ALL}{Fore.BLUE}{' ' * level}{name}/{Style.RESET_ALL}")

def print_file(name, level):
    print(f"{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{' ' * level}{name}{Style.RESET_ALL}")

def list_dir(dir, level = 0):
    for line in Path(dir).iterdir():
        if line.is_dir():
            print_folder(line.name, level);
            list_dir(line, level + 3)
        else:
            print_file(line.name, level)


list_dir(folder)



