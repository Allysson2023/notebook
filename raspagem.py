# pip install requests types-requests bs4

import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/politica/noticia/2025/03/24/o-que-acontece-se-bolsonaro-e-aliados-virarem-reus-veja-o-que-estara-em-jogo-no-stf-nesta-terca.ghtml'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)