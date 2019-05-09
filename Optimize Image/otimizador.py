import tinify
import xlrd
import os
from urllib.parse import urlsplit
import requests
tinify.key = '5p5UxEJn7z5jYohyzUzpqeCJ3Ymbadxj'

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'links.xlsx'
path = os.path.join(pre, fname)
book = xlrd.open_workbook(path)
print("Número de abas: ", book.nsheets)
print("Nomes das Planilhas:", book.sheet_names())
sh = book.sheet_by_index(0)
print(f'Nome: {sh.name}, Linhas: {sh.nrows}, Colunas: {sh.ncols}')
for rx in range(sh.nrows):

    linha = str(sh.row(rx))
    lixo1, url, lixo2 = linha.split("'")
    parts = urlsplit(url)
    paths = parts.path.split('/')
    page = requests.get(url)
    print(url)
    statusCode = page.status_code
    print('Status Code:',statusCode)
    if statusCode == 404:
        os.system("pause")
    source = tinify.from_url(url)
    source.to_file(paths[-1])
