#!/bin/ptyhon3
# 代理
#import urllib.request
import random
import requests

url1 = 'https://api.ip.sb/geoip'
url2 = 'http://httpbin.org/ip'
proxy_http = [
    'http://110.40.13.5:80',
    'http://221.7.255.168:8080'
]
proxy_https = [
    'https://183.129.207.80:21776',
    'https://119.31.210.170:7777'
]

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
req = requests.get(url1, proxies={'http': random.choice(proxy_http), 'https': random.choice(proxy_https)}, headers=headers, timeout=10)
print (req.json())