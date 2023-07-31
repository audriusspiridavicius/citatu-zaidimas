import requests
from bs4 import BeautifulSoup


class AboutQuote:
    def __init__(self, url):
        self.url = url

        response = requests.get(self.url)
        self.html = BeautifulSoup(response.text,"html.parser")

    @property
    def born(self):
        return self.html.find(class_="author-born-location").text

