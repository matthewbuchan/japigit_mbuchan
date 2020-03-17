import urllib.request
import json

i = 0
fileName = 'japi.out'
def getStockData(userVal):
    alphaURL = 'https://www.alphavantage.co/query'
    stockQUO = 'function=GLOBAL_QUOTE'
    stockSYM = 'symbol='+userVal
    APIKey = 'apikey=1D7G82OCHI0ZF7CD'
    stockStr = alphaURL + "?" + stockQUO + "&" + stockSYM + "&" + APIKey
    connection= urllib.request.urlopen(stockStr)
    data = json.load(connection)
    stockDict = {}
    f = open(fileName, "a")
    f.write("\n-------"+userVal+"-------\n")
    
    for i in data:        
        for j in data[i]:            
            jtext = j.split('. ')
            stockDict[jtext[1]] = data[i][j]
            print(jtext[1]+":"+data[i][j])            
            f.write(jtext[1]+":"+data[i][j]+"\n")
                        
    print("The current price of "+stockDict['symbol']+" is: "+stockDict['price']+"\n")
    f.write("The current price of "+stockDict['symbol']+" is: "+stockDict['price']+"\n")
    f.close()
        
while(i == 0):
    uVal = input("Please enter your stock symbol: ").lower()
    if(uVal != 'quit'):
        getStockData(uVal)
        print("\n")
    else:
        i = 1
