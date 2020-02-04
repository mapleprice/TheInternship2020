from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    url = "https://theinternship.io/"
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, features="html.parser")
    logos = soup.find_all("img", class_="center-logos")
    for logo in logos:
        print(logo['src'])
