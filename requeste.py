import requests

url = 'https://g1.globo.com/politica/noticia/2025/03/24/o-que-acontece-se-bolsonaro-e-aliados-virarem-reus-veja-o-que-estara-em-jogo-no-stf-nesta-terca.ghtml'

response = requests.get(url)

print(response.text)