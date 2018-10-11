#!/bin/python3
# IP或域名物理地址查询&html正则匹配
import sys
import random
from pyquery import PyQuery as pq

# ipORhost = sys.argv[1]
ipORhost = 'baidu.com'
url = 'http://ip138.com/ips138.asp?ip=%s&action=2' % ipORhost
headers = {
    'Host': 'ip138.com',
    'Referer': 'http://ip138.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

proxy_http = [
    'http://110.40.13.5:80',
    'http://221.7.255.168:8080'
]
proxy_https = [
    'https://183.129.207.80:21776',
    'https://119.31.210.170:7777'
]

try:
    doc = pq(url, proxies={'http': random.choice(proxy_http), 'https': random.choice(proxy_https)}, headers=headers, method='get', encoding='gb2312')
    print (doc('h1').text())
    for i in doc('li'):
        data = pq(i).text()
        print(data)
except:
    print ('由于免费接口限制，请5秒后重新尝试！\n')