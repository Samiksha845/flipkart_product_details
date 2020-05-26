import io
import csv
import requests
from bs4 import BeautifulSoup

url1 = 'https://www.flipkart.com/search?q=mi%20phones&'
headers = ['Name', 'Pricing']
products = []
prices = []

for i in range(1, 14):
    url2 = 'https://www.flipkart.com/search?q=mi+phones&page={}'.format(i)
    page = requests.get(url1, url2)
    soup = BeautifulSoup(page.text, "html.parser")

    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
        products.append(name.text)
        prices.append(price.text)

record_list = [list(item) for item in list(zip(products, prices))]
print(record_list)

with io.open('C:/Users/SAMIKSHA SENGAR/Documents/web scraping/products.csv', 'w', encoding="utf-8") as fp:
    csv_writer = csv.writer(fp)
    csv_writer.writerow(headers)
    csv_writer.writerows(record_list)
