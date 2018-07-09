urlv1 = "https://api.bitfinex.com/v1"

fp = open("keys.txt")

api_key = str.replace(fp.readline().rstrip(),'api_key=','')
api_secret = str.replace(fp.readline().rstrip() ,'api_secret=','')