#recuperar inf bitfinex
import requests
import string
#from nt import replace
import json
import simplejson as json

#Recupera todas as moedas/compras
v1_url = "https://api.bitfinex.com/v1"
v2_url = "https://api.bitfinex.com/v2"
v_ListCoinCompare = 'tBTCUSD,tLTCUSD,tLTCBTC,tETHUSD,tETHBTC,tETCUSD,tETCBTC,tRRTUSD,tRRTBTC,tZECUSD,tZECBTC,tXMRUSD,tXMRBTC,tDSHUSD,tDSHBTC,tXRPUSD,tXRPBTC,tIOTUSD,tIOTBTC,tEOSUSD,tEOSBTC,tSANUSD,tSANBTC,tOMGUSD,tOMGBTC,tBCHUSD,tBCHBTC,tNEOUSD,tNEOBTC,tETPUSD,tETPBTC,tQTMUSD,tQTMBTC,tAVTUSD,tAVTBTC,tEDOUSD,tEDOBTC,tBTGUSD,tBTGBTC,tDATUSD,tDATBTC,tQSHUSD,tQSHBTC,tYYWUSD,tYYWBTC,tGNTUSD,tGNTBTC,tSNTUSD,tSNTBTC,tBATUSD,tBATBTC,tMNAUSD,tMNABTC,tFUNUSD,tFUNBTC,tZRXUSD,tZRXBTC,tTNBUSD,tTNBBTC,tSPKUSD,tSPKBTC'

#Lttps://api.bitfinex.com/v2/tickers?symbols=tBTCUSD,tLTCUSD,fUSD
v_url_tickers = str(v2_url) + "/tickers?symbols=" + str(v_ListCoinCompare)
#print(str(v_url_tickers))

#recupera lista com tickers
v_tickers = requests.request("GET", v_url_tickers)

#Cria list
m_tickers = v_tickers.json()

#layout - SYMBOL, BID, BID_SIZE, ASK, ASK_SIZE, DAILY_CHANGE, DAILY_CHANGE_PERC, LAST_PRICE, VOLUME, HIGH, LOW
v_BIDBTCUSD = m_tickers[0][1] #Venda
v_ASKBTCUSD = m_tickers[0][3] #Compra


i = 1 # inicia no 1 para pular o primeiro registro referente ao valor do BTCUSD
v_ALT1 = 0
v_ALT2 = 0
v_ASKALTUSD = 0.00 #Valor de compra da altcoin com o BTC
v_BIDALTUSD = 0.00 #Valor de Venda da altcoin para USD

v_ASKALTBTC = 0.00
v_BIDALTBTC = 0.00

while (i < 60):
    print(m_tickers[i][0][])

    if(m_tickers[i][0][] == 'BTC'):
 #Recupera o nome da moeda
 v_ALT1 = m_tickers[i][0][:4]
 #Recupera o valor de venda ALT para BTC
 v_BIDALTBTC = m_tickers[i][1]
 #Recupera o valor de compra do ALT com BTC
 v_ASKALTBTC =  m_tickers[i][3]
 #print('pBTC', v_ASKBTCALT);
    elif (m_tickers[i][0][] == 'USD'): 
 #Recupera o nome da moeda
 v_ALT2 = m_tickers[i][0][:4]
 #Recupera o valor de venda ALT para USD
 v_BIDALTUSD = m_tickers[i][1]
 #recupera o valor de Venda para USD
 v_ASKALTUSD = m_tickers[i][3]

 #print('pUSD', v_BIDALTUSD);
    else:
 print('ERRO');

    #print(v_ALT1, v_ALT2)

    if(v_ALT1 == v_ALT2):
print(v_ALT1, ' USD -> BTC -> ALT -> USD:', v_ASKBTCUSD / ((1.00 /v_ASKALTBTC) * v_BIDALTUSD) *100)
print(v_ALT1, ' USD -> ALT -> BTC -> USD:', 100.00 / (((100.00 /v_ASKALTUSD) * v_BIDALTBTC) * v_BIDBTCUSD) *100)

#print('v_ASKBTCUSD:', v_ASKBTCUSD)
#print('v_BIDBTCUSD:', v_BIDBTCUSD)
#print('v_ASKBTCALT:' ,v_ASKBTCALT)
#print('v_BIDALTUSD:', v_BIDALTUSD);

    i = i+1;

    

#index()
#m_tickers.append(0)

#print (m_tickers)

#print(m_tickers[0].index('10680'))


#livros.append('Android')




#print(v_tickers)
#print (m_tickers[1])
#a = m_tickers[0]
#print(a)
#print v_tickers[0][1]
#print(str(len(str(v_tickers))))


#url = "https://api.bitfinex.com/v1/pubticker/btcusd"

#response = requests.request("GET", url)

#print(response.text)
