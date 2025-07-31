import os
import time
from termcolor import colored
from pyfiglet import figlet_format

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(colored(figlet_format("Wide", font="slant"), "cyan"))
    print(colored("🔍 Information Gathering Tools", "yellow"))
    print(colored("Author: Affan SUhendar | Version: 1.0\n", "green"))


def main():
    clear_screen()
    banner()

if __name__ == "__main__":
    main()
