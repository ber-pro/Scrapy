from peewee import *
import csv

db = PostgresqlDatabase(database='test', user='postgres', password='1', host='localhost')


class Coin(Model):
    name = TextField()
    url = TextField()
    description = TextField()
    traffic = CharField()
    persent = CharField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Coin])

    with open('liteintet.csv') as f:
        order = ['name', 'url', 'description', 'traffic', 'persent']
        reader = csv.DictReader(f, fieldnames=order)
        coins = list(reader)

        # for row in coins:
        #	coin=Coin(name=row['name'],url=row['url'],description=row['description'],traffic=row['traffic'],persent=row['persent'])
        #	coin.save()

        with db.atomic():
            for row in coins:
                Coin.create(**row)


if __name__ == '__main__':
    main()
