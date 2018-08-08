import xlsxwriter
import json
import requests

start = 1
f = 1
convert = 'USD'

crypto_workbook = xlsxwriter.Workbook('price_graph.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Price')

for i in range(10):
    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&start=' + str(start)

    request = requests.get(ticker_url)
    results = request.json()
    data = results['data']

    for currency in data:
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quotes'][convert]
        price = quotes['price']

        crypto_sheet.write(f,0,name)
        crypto_sheet.write(f,1,symbol)
        crypto_sheet.write(f,2,str(price))

        f += 1

    start += 100

crypto_workbook.close()
