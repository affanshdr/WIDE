import socket
import requests
import pprint
import json
from termcolor import colored
from utils import teks_warna

def Intro(Judul):
    print(teks_warna(("+")+("-"*(len(Judul)+2))+("+"),"blue"))
    print(teks_warna(f"| {Judul} |","blue"))
    print(teks_warna(("+")+("-"*(len(Judul)+2))+("+"),"blue"))

def checkip():
    Intro("Mencari IP dan Lokasi sebuah domain")

    print(teks_warna("Contoh Hostname : google.com", "yellow"))
    hostname = (input(teks_warna("Input Hostname  : ", "yellow")))
    ip_address = socket.gethostbyname(hostname)

    url = "https://geolocation-db.com/jsonp/" + ip_address
    response = requests.get(url)
    geolocation = response.content.decode()
    geolocation = geolocation.split("(")[1].strip(")")
    geolocation = json.loads(geolocation)


    print("\n")
    print(f"Info Hostname dari {hostname}")
    print(ip_address)

    for k,v in geolocation.items():
        print(teks_warna(f"{k}: {v}", "green"))

    print("\n")