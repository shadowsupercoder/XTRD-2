import json
import requests

from xtrd.celery import app

from .models import Etherscan, Coinmarketcap

@app.task
def parse_data():
    r = requests.get('https://api.coinmarketcap.com/v2/ticker/3067/')
    data = json.loads(r.text)['data']
    usd_price = data['quotes']['USD']['price']
    volume_24h = data['quotes']['USD']['volume_24h']
    # Etherscan 
    # api_key = 'N3QTTMJDC2NEM86D3ZP7H8N4PVJSXSWN4Y'
    obj = Coinmarketcap.objects.create(
        price_usd=usd_price,
        price_eth=usd_price,
        volume=volume_24h)
    print(obj.id)
