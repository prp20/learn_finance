import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[0].find_all('spans')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts

def real_time_stock():
    url = "https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch"
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, "My(6px) Pos(r) smartphone_Mt(6px)")
        if texts != []:
            price, change = texts[0], texts[1]
        else:
            price, change = [],[]
    except ConnectionError():
        price, change = [],[]
    return price, change

print(real_time_stock())