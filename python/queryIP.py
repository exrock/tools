#!/bin/python3
# IP或域名物理地址查询&html正则匹配
import requests
import re
import sys

ipORhost = sys.argv[1]
url = 'http://ip138.com/ips138.asp?ip=%s&action=2' % ipORhost
headers = {
    'Host': 'ip138.com',
    'Referer': 'http://ip138.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

try:
    req = requests.get(url, headers=headers, timeout=10)
    req.encoding = 'gb2312'

    if re.findall(r'(\d\.){3}\d', ipORhost):
        res_h1 = re.compile(r'<h1>(.*?)</h1>', re.S|re.M)
    else:
        res_h1 = re.compile(r'<font.*\"blue\">(.*?)</font>', re.S|re.M)
    result_h1 = res_h1.findall(req.text)
    res_li = re.compile(r'<li>(.*?)</li>', re.S|re.M)
    result_li = res_li.findall(req.text)

    result = result_h1 + result_li
    for i in result:
        print (i)
except:
    print ('由于免费接口限制，请5秒后重新尝试！\n')