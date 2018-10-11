#!/bin/python3
# 百度翻译
import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容：')

# url = 'https://fanyi.baidu.com/v2transapi'
url = 'http://fanyi.baidu.com/basetrans'

data = {
'from': 'zh',
'to': 'en',
'query': content,
}

head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

data = urllib.parse.urlencode(data).encode('utf-8') 
request = urllib.request.Request(url, data, head)
html = urllib.request.urlopen(request).read()
print (html)
# html = json.loads(html)
# print (html)