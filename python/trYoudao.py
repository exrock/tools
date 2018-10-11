#!/bin/python3
# 有道翻译
import urllib.request
import urllib.parse
import json
import sys

# content = input('请输入要翻译的内容：')
content = sys.argv[1]
data = {
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}
data = urllib.parse.urlencode(data).encode('utf-8')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

response = urllib.request.Request(url, data, head)
html = urllib.request.urlopen(response).read().decode('utf-8')
html = json.loads(html) 
print ('翻译结果：\n%s' % (html['translateResult'][0][0]['tgt']))