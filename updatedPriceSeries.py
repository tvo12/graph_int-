import xlsxwriter
import json
import requests
import random
import datetime
import time



#########################
### Define Functions ####
#########################


# This function creates Random Price within +/-10% of a given price
# Question - why do you think this is useful?
def nextPrice(currentPrice):
    return (currentPrice * (1 + random.randint(-200, 200)/2000))


#  This function gets the current price of a given currency
#  See Lesson 16 for an answer to your question on picking on specific currency


def getCryptoPrice(currencyID):
    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(currencyID) + '/?structure=array'

    request = requests.get(ticker_url)
    results = request.json()
    data = results['data'][0]


    price = quotes['price']

    return(price)

#####################
####  Run Script ####
#####################

start = 1
f = 1
convert = 'USD'
delayInSeconds = 2
maxLoops = 50

crypto_workbook = xlsxwriter.Workbook('price_graph3.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Price')

currencyID = 1


ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(currencyID) + '/?structure=array'

request = requests.get(ticker_url)
results = request.json()
data = results['data']
currency = data[0]

name = currency['name']
symbol = currency['symbol']
quotes = currency['quotes'][convert]
price = quotes['price']


print(price)

loopCounter = 0
while loopCounter < maxLoops:

    price = nextPrice(price)
#    price = getCryptoPrice(currencyID)

    print (f)
    print (loopCounter)
    print(price)

    #write to sheet
    crypto_sheet.write(f,0,name)
    crypto_sheet.write(f,1,symbol)
    crypto_sheet.write(f,2,price)

    loopCounter += 1
    f += 1

    time.sleep(delayInSeconds)


print (f)
print (loopCounter)
print ('Closing Book')
crypto_workbook.close()





    
currentPrice = 12.0
newPrice = nextPrice(currentPrice)

print (currentPrice)
print (newPrice)
