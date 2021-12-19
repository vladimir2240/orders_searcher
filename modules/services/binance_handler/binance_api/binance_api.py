import urllib
import requests
from urllib.parse import urlparse

class BinanceCall:
    methods = {
        'tickerPrice': {'url': 'api/v3/ticker/price', 'method': 'GET', 'private': False},
    }

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            kwargs.update(command=name)
            return self.call_api(**kwargs)

        return wrapper

    def call_api(self, **kwargs):
        command = kwargs.pop('command')
        api_url = f'https://api.binance.com/{self.methods[command]["url"]}'

        payload = kwargs
        headers = {}

        payload_str = urllib.parse.urlencode(payload)

        if self.methods[command]['method'] == 'GET' or self.methods[command]['url'].startswith('sapi'):
            api_url += '?' + payload_str

        response = requests.request(method=self.methods[command]['method'], url=api_url,
                                    data="", headers=headers)

        if 'code' in response.text:
            print(response.text)
        return response.json()
