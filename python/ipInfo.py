#!/usr/bin/env python3

import sys
import re

try:
    import requests
except:
    try:
        import os
        os.system('pip install requests')
        import requests
    except:
        exit('请确认是否有权限安装第三方库!\n退出!')

qip = 'http://ip-api.com/json/%s' % '223.5.5.5' #sys.argv[1]
req = requests.get(qip)

dic = {
    'as': '所属公司',
    'city': '城市',
    'country': '国家',
    'countryCode': '国家代码',
    'isp': '服务商',
    'lat': '纬度',
    'lon': '经度',
    'org': '机构',
    'query': '查询',
    'region': '地区码',
    'regionName': '地区名称',
    'status': '状态',
    'timezone': '时区',
    'zip': '邮编'
}

def align(string, length = 0):
    if length == 0:
        return string
    regZH = re.compile(r'[\u4e00-\u9fff]+', re.UNICODE)
    if regZH.findall(string):
        ph = '　'
    else:
        ph = ' '

    slen = len(string)
    while slen < length:
        string += ph
        slen += 1

    return string

print ('查询结果：')
for k, v in req.json().items():
    key = dic.get(k)
    print ('  ', align(key, 6)+str(v))
