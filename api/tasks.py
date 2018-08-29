import json
import requests
# import etherdelta

from xtrd.celery import app

from .models import Etherscan, Coinmarketcap, Idex


@app.task
def parse_data():
    ETH_USD = float(requests.get(
        'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()['USD'])
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/3067/')
    data = json.loads(r.text)['data']
    usd_price = data['quotes']['USD']['price']
    eth_price = float(usd_price) / ETH_USD
    volume_24h = data['quotes']['USD']['volume_24h']
    # Etherscan 
    # api_key = 'N3QTTMJDC2NEM86D3ZP7H8N4PVJSXSWN4Y'
    obj_c = Coinmarketcap.objects.create(
        price_usd=usd_price,
        price_eth=eth_price,
        volume=volume_24h)
    print("Created coinmarketcap obj: " + str(obj_c.date))

    r = requests.post('https://api.idex.market/returnTicker')
    data = r.json()['ETH_XTRD']
    volume = data['baseVolume']
    eth_price = float(data['last'])
    usd_price = eth_price * ETH_USD

    obj_i = Idex.objects.create(
        price_usd=usd_price,
        price_eth=eth_price,
        volume=volume)
    print("Created IDEX obj: " + str(obj_i.date))

    # initialize client
    # client = etherdelta.Client()
    # symbol = 'XTRD'
    # ticker = client.get_ticker(symbol)
    # volume = ticker['baseVolume']
    # eth_price = float(ticker['last'])
    # usd_price = eth_price * ETH_USD

    # obj_e = EtherDelta.objects.create(
    #     price_usd=usd_price,
    #     price_eth=eth_price,
    #     volume=volume)
    # print("Created EtherDelta obj: " + str(obj_e.date))

