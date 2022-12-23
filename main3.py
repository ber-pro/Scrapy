import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['url'],
                         data['price']])


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_="cmc-table cmc-table___11lFC cmc-table-homepage___2_guh").find('tbody').find_all(
        'tr')

    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) == 11:
            name = tds[2].find('a').text
            url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
            price = tds[3].text

            data = {'name': name,
                    'url': url,
                    'price': price}
            write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
