
import requests
import json
import simplejson as json
import base64
import hmac
import hashlib
import time
import sys, os
import ccxt
import string
import pandas as pd
import numpy as np

#orderbook: https://api.bitfinex.com/v1/book/btcusd
#ticker: https://api.bitfinex.com/v1/pubticker/btcusd
#candles: https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist
#https://api.bitfinex.com/v2/candles/trade:5m:tBTCUSD/hist?start=1434764470000&end=1497922870000


#__all__ = ['ticker', 'today', 'orderbook', 'lendbook', 'stats', 'trades', 'lends', 'symbols', 'place_order', 'delete_order', 'delete_all_order', 'status_order', 'active_orders', 'active_positions', 'place_offer', 'cancel_offer', 'status_offer', 'active_offers', 'past_trades', 'balances', 'claim_position', 'close_position', 'withdraw']
urlv1 = "https://api.bitfinex.com/v1"
urlv2 = "https://api.bitfinex.com/v2"

fp = open("keys.txt")
# fp = open("../keys.txt")

#leitura dos parâmetros do arquivo keys.txt
btc_short = int(str.replace(fp.readline().rstrip(),'btc_short=',''))
btc_long = int(str.replace(fp.readline().rstrip() ,'btc_long=',''))
time_interval = str.replace(fp.readline().rstrip() ,'time_interval=','')
btc_valor_cmp_vda = int(str.replace(fp.readline().rstrip() ,'btc_valor_cmp_vda=',''))
btc_size_candle = int(str.replace(fp.readline().rstrip(),'btc_size_candle=',''))


def getParametros():
    os.system('clear')

    print (" >>>>>>>>>>>> Parâmetros <<<<<<<<<<<<<  \n")
    print (" Bitcoin - short: " + str(btc_short))
    print (" Bitcoin - long: " + str(btc_long))
    print (" Bitcoin - intervalo de tempo: " + str(time_interval))
    print (" Bitcoin - período histórico: " + str(btc_size_candle))
    print (" Bitcoin - valor compra/venda: $" + str(btc_valor_cmp_vda))
    #print ("Sua chave privada: " + str(API_SECRET))

#FUNÇÃO CRIA MENU PRINCIPAL
def main_menu_ini():
    os.system('clear')
    getParametros()

    print("\n >>>> Bem vindo ao TraderCoin <<<< \n \n 1.Visualizar preço atualizado \n 2.Visualizar ordens \n 3.Visualizar Últimas posições \n 4.Iniciar trader \n 5.Sair \n")     
    choice = input("Opção: ")

    if choice == "1":
        print ("Menu 1 foi selecionado.")
        getTicker('btcusd')
        input("Pressione Enter p/ continuar...")
        main_menu_ini()
    elif choice == "2":
        print ("Menu 3 foi selecionado.")
        getTicker('btcusd')
        input("Pressione Enter p/ continuar...")
        main_menu_ini()
    elif choice == "3":
        print ("Menu 2 foi selecionado.")
        getHistCandles('btcusd')
        input("Pressione Enter p/ continuar...")
        main_menu_ini()
    elif choice == "4":
        print ("Menu 4 foi selecionado.")
        getCalculaEmacross('btcusd')
        input("Pressione Enter p/ continuar...")
        main_menu_ini()
    elif choice == "5":
        quit()
    else:
    # Any integer inputs other than values 1-5 we print an error message
        print("Opção errada, tente novamente...")
        main_menu_ini()
    return

def quit():
  raise SystemExit()

def getTicker(coin):
    a = 1
    try:
        while a == 1:
            if (coin == 'btcusd'):
                r = requests.get(urlv1 + "/pubticker/" + "btcusd", verify=True)
                rep = r.json()
                lastprice = rep['last_price']
                lowprice = rep['low']
                highprice = rep['high']
                print (" Último preço: " + lastprice + "\n Menor Preço(24h): " + lowprice  + "\n Maior Preço(24h): " + highprice)

            elif (coin == 'ethusd'):
                r = requests.get(urlv1 + "/pubticker/" + "ethusd", verify=True)
                rep = r.json()
                lastprice = rep['last_price']
                lowprice = rep['low']
                return lastprice, lowprice, highprice
                main_menu_ini()

            elif (coin == 'iotusd'):
                r = requests.get(urlv1 + "/pubticker/" + "iotusd", verify=True)
                rep = r.json()
                lastprice = rep['last_price']
                lowprice = rep['low']
                return lastprice, lowprice, highpriceb
                main_menu_ini()
            else:
                return "Nenhum preço foi informado."
            break
    except KeyboardInterrupt:
        pass

def getTest():
    from_datetime = '2017-01-01 00:00:00'
    from_timestamp = exchange.parse8601(from_datetime)
    print(from_timestamp)
    #print(ccxt.exchanges)

def getHistCandles(coin):
    cont = 0
    qtd_per = 0

    while True:
        try:
            if (coin == 'btcusd'): 
                r = requests.get(urlv2 + "/candles/trade:" + time_interval +"m:tBTCUSD/hist?")
                data = r.json()

                while qtd_per < btc_size_candle:
                    qtd_per = qtd_per + 1
                    lista = data[qtd_per]
                    #Parâmetros API [0-MTS, 1-OPEN, 2-CLOSE, 3-HIGH, 4-LOW, 5-VOLUME]
                    preco_high = lista[3] 
                    preco_low = lista[4] 
                    preco_vol = lista[5] 
                    preco_fecha = lista[2] 
                    preco_data_epoch = lista[0]
                    preco_data_formatado = time.strftime('%d/%m/%Y %H:%M:%S',  time.localtime(preco_data_epoch/1000.))
                    print (" Time: " + preco_data_formatado + " - Preço " + str(round(preco_fecha)) + " - High " + str(round(preco_high)) + " - Low " + str(round(preco_low)) + " - Vol " + str(preco_vol))

            break
        except ValueError:
            return

def getCalculaEmacross(coin):

    while True:
        try:
            if (coin == 'btcusd'): 
                #params = { 'start': 1516293900000, 'end': 1516329000000 } #datas
                #r = requests.get(urlv2 + "/candles/trade:" + time_interval +"m:tBTCUSD/hist?", params = params)
                r = requests.get(urlv2 + "/candles/trade:" + time_interval +"m:tBTCUSD/hist?")
                data = r.json()

                cont = 0
                qtd_per_short = 0
                preco_fecha = 0
                idx = 0

                lista_preco_fecha = []
                lista_preco_data = []

                for i in range (btc_short):
                    qtd_per_short = qtd_per_short + 1
                    lista = data[qtd_per_short] #recupera todos os grupos de preço de cada horário
                    preco_fecha = lista[2] #recupera o preço de fechamento
                    data_epoch = lista[0]
                    lista_preco_fecha.append(int(preco_fecha))
                    lista_preco_data.append(int(data_epoch))
                
                #calcula o preço médio exponencial (ema cross) do período curto
                df_preco_short = pd.DataFrame(lista_preco_fecha) #cria dataframe de preço de fechamento
                df_preco_short.columns = ['preco_fecha'] #renomeia columa do dataframe com o preco de fechamento
                df_preco_short.insert(loc=idx, column='data_epoch', value=lista_preco_data) #insere coluna de data epoch
                df_preco_short = df_preco_short.sort_values(['data_epoch', 'preco_fecha'], ascending=[True, False])
                #df_preco_short = df_preco_short.reset_index(drop = True)
                df_ema_preco_short = df_preco_short['preco_fecha'].ewm(com=0.5).mean()
                df_ema_preco_short.sort_index(inplace=True) #reordenação para o penúltimo preço
                ult_ema_short = round(df_ema_preco_short.iloc[0],3)#recupera o primeiro registro na posição 0

                cont = 0
                qtd_per_long = 0
                preco_fecha_long = 0
                idx_long = 0

                lista_preco_fecha_long = []
                lista_preco_data_long = []

                for i in range (btc_long):
                    qtd_per_long = qtd_per_long + 1
                    lista_long = data[qtd_per_long] #recupera todos os grupos de preço de cada horário
                    preco_fecha_long = lista_long[2] #recupera o preço de fechamento
                    data_epoch_long = lista_long[0]
                    lista_preco_fecha_long.append(int(preco_fecha_long))
                    lista_preco_data_long.append(int(data_epoch_long))
                
                #calcula o preço médio exponencial (ema cross) do período curto
                df_preco_long = pd.DataFrame(lista_preco_fecha_long) #cria dataframe de preço de fechamento
                df_preco_long.columns = ['preco_fecha'] #renomeia columa do dataframe com o preco de fechamento
                df_preco_long.insert(loc=idx_long, column='data_epoch', value=lista_preco_data_long) #insere coluna de data epoch
                df_preco_long = df_preco_long.sort_values(['data_epoch', 'preco_fecha'], ascending=[True, False])
                #df_preco_short = df_preco_short.reset_index(drop = True)
                df_ema_preco_long = df_preco_long['preco_fecha'].ewm(com=0.5).mean()
                df_ema_preco_long.sort_index(inplace=True) #reordenação para o penúltimo preço
                ult_ema_long = round(df_ema_preco_long.iloc[0],3)

                if ult_ema_short >= ult_ema_long:
                    print(" Preço Short: " + str(ult_ema_short))
                    print(" Preço Long: " + str(ult_ema_long))
                    print(" Comprar...")
                else:
                    print(" Preço Short: " + str(ult_ema_short))
                    print(" Preço Long: " + str(ult_ema_long))
                    print(" Vender...")

            break
        except ValueError:
            return


