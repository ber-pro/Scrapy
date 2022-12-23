import csv
from peewee import *

db = PostgresqlDatabase(database='vladislav', user='postgres', password='1', host='localhost')


class Coin(Model):
    name = CharField()
    url = TextField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Coin])

    with open('cmc.csv') as f:
        order = ['name', 'url']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # for row in coins:
        #   coin=Coin(name=row['name'],url=row['url'])
        #  coin.save()
        with db.atomic():
            for row in coins:
                Coin.create(**row)


if __name__ == '__main__':
    main()
