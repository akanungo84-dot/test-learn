import requests
from bs4 import BeautifulSoup


def fetch_menu_text(url:str)->str:
    html=requests.get(url,timeout=30).text
    soup=BeautifulSoup(html,'html.parser')
    return soup.get_text('\n',strip=True)[:100000]
