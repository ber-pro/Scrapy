import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def writer_csv(data):
    with open('10.csv', 'a') as f:
        order = ['since', 'author']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_article(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts


def get_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text
        except:
            author = ''
        data = {'author': author, 'since': since}
        writer_csv(data)


def main():
    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/?themify_builder_infinite_scroll=yes'.format(
            str(page))
        articles = get_article(get_html(url))

        if articles:
            get_data(articles)
            page = page + 1
        else:
            break


if __name__ == '__main__':
    main()
