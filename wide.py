import os
import time
from termcolor import colored
from pyfiglet import figlet_format
from utils import teks_warna

from garap_email import garap_email
from CheckIP import checkip

# System
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(colored(figlet_format(" Wide", font="slant"), "cyan"))
    print(colored("🔍 Information Gathering Tools", "yellow"))
    print(colored("Author: Affan SUhendar | Version: 1.0\n", "green"))

def option():
    print(teks_warna(f"[+] Mencari IP dan Lokasi sebuah domain", "blue"))
    print(teks_warna(f"[+] Email Scrapper sebuah domain", "blue"))
    print(teks_warna(f"[+] Checking ...", "blue"))
    print(teks_warna(f"[+] Checking ...", "blue"))
    print(teks_warna(f"[+] Exit", "blue"))

def main():
    clear_screen()
    banner()


if __name__ == "__main__":

    main()

    while True:

        option()
        Pilihan = int(input(teks_warna("\nPilihan: ", "yellow")))


        match Pilihan :

            case 1:
                checkip()
            case 2:
                garap_email()
            case 3:
                
                print("3")
            case 4:
                break
            case _:
                print("Pilihan Tidak Tersedia")
    

