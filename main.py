import locale
import string
from pathlib import Path
from datetime import datetime

CAMINHO_DO_ARQUIVO = Path(__file__).parent / 'mesalidades.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2025, 10, 20)

dados = dict(
    nome = 'Marcos',
    valor = converte_para_brl(25),
    data = data.strftime('%d/%m'),
)

# ENCODIND  deixa as letra certa do texto 
with open(CAMINHO_DO_ARQUIVO, 'r',encoding='UTF-8' ) as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))