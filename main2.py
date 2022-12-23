import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('pluginc.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')

        writer.writerow([data['name'],
                         data['url'],
                         data['rating']])


def refined(s):
    r = s.split(' ')[0]
    return r.replace(',', '')


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        r = plugin.find('div', class_="plugin-rating").find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'rating': rating}

        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
