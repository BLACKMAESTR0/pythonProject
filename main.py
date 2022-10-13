import requests
from bs4 import BeautifulSoup
import json
import time

def vzyathtml(zzzz,aa='2303'):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
    url = f'https://www.labirint.ru/genres/{aa}/?display=table&page={zzzz}'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return (soup,aa)
def zapis(asas):
    soup=vzyathtml(1)[0]
    slov = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO', 'Ж': 'J', 'З': 'Z', 'И': 'I',
            'Й': 'YO', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SH', 'Ъ': ' ', 'Ы': 'I', 'Ь': ' ',
            'Э': 'E', 'Ю': 'IU', 'Я': 'YA', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'yo', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh',
            'ъ': '*', 'ы': 'i', 'ь': '*', 'э': 'e', 'ю': 'iu', 'я': 'ya', ' ': ' '}
    genre = soup.find('h1', class_='genre-name').text.strip()
    genreeng = ''
    for i in range(len(genre)):
        bukv = slov[genre[i]]
        genreeng += bukv
    named_tuple = time.localtime()
    times = time.strftime("%m/%d/%Y, %H:%M", named_tuple)
    times1 = times.split(',')[1]
    times2 = times.split(',')[0].replace('/', '.')
    nomer=vzyathtml(1)[1]
    filebook = 'labirint.' + nomer+'-'+genreeng + '_' + times1 + '_' + times2 + '.json'
    filebook = filebook.replace(' ', '_')
    shtyk = filebook.find(':')
    filebook = filebook.replace(':', '.')
    filebook = filebook[:shtyk + 3] + '__' + filebook[shtyk + 4:]
    filebook = filebook.replace('*', '')
    print(filebook)
    with open(filebook, 'w', encoding='UTF-8') as file:
        json.dump(asas, file, indent=4, ensure_ascii=False)



def sobratknigi(dada):
    c = 0
    books = []
    for page in range(1, dada + 1):
        soup=vzyathtml(page)[0]
        a = soup.find('tbody', class_="products-table__body").find_all('tr')
        for item in a:
            try:
                naz = item.find('a', class_='book-qtip').text.strip()
            except:
                naz = 'no author'
            try:
                cen = item.find('span', class_='price-val').text.strip()
            except:
                cen = 'no'
            try:
                aut = item.find('td', class_='col-sm-2').text.strip()
            except:
                aut = 'no'
            try:
                skid = item.find('span', class_='price-val')['title'].strip()
            except:
                skid = '-'
            dic = {'title': naz, 'price': cen, 'author': aut, "skidka": skid}
            books.append(dic)
            c += 1
    print(f'Всего книг - {c}')
    return books

def kolvostr():
    soup = vzyathtml(1)[0]
    ssss = int(soup.find('div', class_="pagination-number").find_all('a')[-1].text)
    return ssss




def get_data():

    pages_count=kolvostr()
    knigi=sobratknigi(pages_count)
    zapis(knigi)






get_data()