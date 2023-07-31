import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from AboutPage import AboutQuote
from Quote import Quote

"""
reikia pamodifikuoti programa kad pirmiau sugeneruoti random skaiciu 
ir tada su BeautifulSoup gauti tam tikra citata pagal eile
kad nereiktu parsint visu citatu


"""
class QuotePage:
    # Quote = TypeVar('Quote')
    def __init__(self, page_url='http://quotes.toscrape.com/page/'):
        self.quotes_list = []
        self.url = page_url
        # response = requests.get(self.url)
        # self.html = BeautifulSoup(response.text, "html.parser")

    # def get_quotes(self, id):
    def get_quotes(self, url = ''):
        
        if url:
            response = requests.get(url)
            if not response.ok:
                print('error occured while trying get info from page')
            self.html = BeautifulSoup(response.text, "html.parser")
        # quotes_list = self.html.select(".quote")[id]
        quotes_list = self.html.select(".quote")
        for quote in quotes_list:
         
            # for quote in quotes_list:
            quote_text = quote.find(class_="text").text
            author = quote.find(class_="author")
            link = urljoin(self.url, author.parent.find("a")["href"])
            # print(quote_text)
            # print(author)
            # print(link)

            about_page = AboutQuote(link)

            # print(new_page.born)

            q = Quote(quote_text, author.text, about_page.born)
            self.quotes_list.append(q)
        return self.quotes_list


    def get_quotes_multiple_pages(self, list_of_pages):
        for page in list_of_pages:
            print(page)
            self.get_quotes(f'{self.url}{page}')
            print(f'{page} ok?')
            
            time.sleep(5)
        return self.quotes_list