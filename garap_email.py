from collections import deque
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse
from utils import teks_warna

def garap_email():

    print(teks_warna("Contoh URL   : google.com","yellow"))
    userUrl = input(teks_warna("Masukkan URL : ", "yellow"))
    if not userUrl.startswith(('http://', 'https://')):
        userUrl = 'http://' + userUrl

    urls = deque([userUrl])
    scraped_urls = set()
    emails = set()
    count = 0

    try:
        while urls:
            count += 1
            if count > 20:
                break

            url = urls.popleft()
            scraped_urls.add(url)
            print(teks_warna(f"Mencari : {url}", "green"))

            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
                continue

            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, 'html.parser')

            for anchor in soup.find_all("a"):
                link = anchor.get("href", "")
                if link.startswith('mailto:') or link.startswith('javascript:') or link == "#":
                    continue
                full_link = urllib.parse.urljoin(url, link)
                if full_link not in urls and full_link not in scraped_urls:
                    urls.append(full_link)

    except KeyboardInterrupt:
        print(teks_warna("program berhenti.", "yellow"))

    if emails:
        print(teks_warna("\nEmail Ditemukan:","green"))
        for mail in emails:
            print(teks_warna(mail + "\n", "green"))
    else:
        print(teks_warna("\nTidak Menemukan email.\n","green"))

