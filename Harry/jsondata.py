import json
from urllib.request import urlopen
api_key='ce3d50fb-b75a-4032-83ef-0460b01475e5'
url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
qs='?CMC_PRO_API_KEY=ce3d50fb-b75a-4032-83ef-0460b01475e5'
qurl='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=ce3d50fb-b75a-4032-83ef-0460b01475e5'

with urlopen('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=ce3d50fb-b75a-4032-83ef-0460b01475e5') as res:
    cmcResponse=res.read()

data=json.loads(cmcResponse)
# iJsonData=json.dumps(data,indent=2)
# with open("i_json_data.json",'w') as f:
#     f.write(iJsonData)
# print(iJsonData)
dataListOfDict=data['data']
ccList={}
for cc in dataListOfDict:
    ccList[cc['name']]=cc['quote']['USD']['price']
i=int(input("Number of Cryptocurrencies: "))

#Generating List of Crypto and Rates in USD
genList=[]
tupleList=[]
for x in ccList:
    temp=' '.join([x,str(ccList[x])])
    t=(x,ccList[x])
    genList.append(temp)
    tupleList.append(t)

def price(x):
    return x[-1]

sortedByValue=sorted(tupleList,key=price,reverse=True)

#Printing ith Entries:
for x in range(i):
    print(sortedByValue[x])
print('*'*20)  
for x in range(i):
    print(genList[x])




