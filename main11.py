import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.json()


def main():
    url = 'https://www.youtube.com/browse_ajax?ctoken=4qmFsgJUEhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaOEVnWjJhV1JsYjNNWUF5QUFNQUU0QWVvREYwTm5Ua1JTUld0VFEyZHFSV2cxVjBoNVgzcGljMms0&continuation=4qmFsgJUEhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaOEVnWjJhV1JsYjNNWUF5QUFNQUU0QWVvREYwTm5Ua1JTUld0VFEyZHFSV2cxVjBoNVgzcGljMms0&itct=CAIQybcCIhMIiq2fosnG7gIVh2myCh2miALw'
    print(get_html(url))


if __name__ == '__main__':
    main()
