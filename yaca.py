import requests
from bs4 import BeautifulSoup
import csv


def filter_cy(s):
    return s.split(' ')[-1]


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['snippet'],
                         data['cy']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''

        try:
            url = li.find('a').get('href')
        except:
            url = ''

        try:
            snippet = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            snippet = ''

        try:
            c = li.find('div', class_='yaca-snippet__cy').text
            cy = filter_cy(c)
        except:
            cy = ''

        data = {'name': name,
                'url': url,
                'snippet': snippet,
                'cy': cy}

        write_csv(data)


def main():
    pattern = 'https://yacca.ru/cat/Entertainment/{}.html'
    for i in range(1, 5):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
