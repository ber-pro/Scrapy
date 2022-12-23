import requests
import csv


def get_text(url):
	r=requests.get(url)
	return r.text

def writer_csv(data):
	with open('liteintet.csv','a') as f:
		order=['name','url','description','traffic','percent']
		writer=csv.DictWriter(f,fieldnames=order)
		writer.writerow(data)




def main():

	for i in range(0,6495):

		url='https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
		respons=get_text(url)
		data=respons.strip().split('\n')[1:]
		
		for row in data:
			columns=row.strip().split('\t')
			name=columns[0]
			url=columns[1]
			description=columns[2]
			traffic=columns[3]
			percent=columns[4]

			data={'name':name,
				  'url':url,
				  'description':description,
				  'traffic':traffic,
				  'percent':percent}
			writer_csv(data)

if __name__ == '__main__':
	main()