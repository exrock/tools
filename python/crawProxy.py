#!/usr/bin/env python3
# 抓取西刺代理网站高匿代理
import json
from pyquery import PyQuery as pq


class GetProxy(object):
    userAgents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]
    outputTitle = ['国家', '类型', 'IP地址', '端口', '服务器地址', '是否匿名', '延迟', '验证日期']
    from_url = 'http://www.xicidaili.com/nn'

    def get_ip_list(self):
        import random
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Host': 'www.xicidaili.com',
            'Pragma': 'no-cache',
            'Referer': 'http://www.xicidaili.com/',
            'User-Agent': random.choice(self.userAgents)
        }

        req = pq(self.from_url, headers=headers, timeout=3)

        # tr = 0, 获取的数据第一行为标题栏,排除
        tr = 0
        item = {}
        lines = []
        for i in req.items('tr'):
            # item = {}必须在循环内重新初始化,否则函数返回的结果是:lines中的元素全都为最后一次循坏获取的
            item = {}
            if tr < 1:
                tr += 1
                continue
            else:
                # 国家
                item[self.outputTitle[0]] = i('td>img').attr('alt')
                # 类型
                item[self.outputTitle[1]] = i('td').eq(5).text()
                # IP地址
                item[self.outputTitle[2]] = i('td').eq(1).text()
                # 端口
                item[self.outputTitle[3]] = i('td').eq(2).text()
                # 服务器地址
                item[self.outputTitle[4]] = i('td').eq(3)('a').text()
                # 是否匿名
                item[self.outputTitle[5]] = i('td').eq(4).text()
                lines.append(item)
        return lines

    def verify_ip(self, arg1, arg2, arg3):
        import random
        import requests
        verify_url = 'http://httpbin.org/ip'
        proxies = {'http': '%s://%s:%s' % (arg1, arg2, arg3), 'https': '%s://%s:%s' % (arg1, arg2, arg3)}
        # proxies = {'http': 'http://118.190.95.35:9001', 'https': 'http://118.190.95.35:9001'}
        headers = {'User-Agent': random.choice(self.userAgents)}
        try:
            req = requests.get(verify_url, proxies=proxies, headers=headers, timeout=3)
            timeout = ('%.2f秒' % (req.elapsed.microseconds / 10 ** 6))
            return timeout
        except:
            pass

    def verify_ip_list(self):
        ip_list = self.get_ip_list()
        proxy_list = []
        for i in ip_list:
            # 类型
            proxy_type = i['类型'].lower()
            # IP地址
            proxy_ip = i['IP地址']
            # 端口
            proxy_port = i['端口']
            timeout = self.verify_ip(proxy_type, proxy_ip, proxy_port)
            if timeout:
                i['延迟'] = timeout
                proxy_list.append(i)
            else:
                continue
        return proxy_list

    # def rep_get_ip(self):
    #     results = self.verify_ip_list()
    #     n = 0
    #     while True:
    #         if len(results) < 2000:
    #             n += 1
    #             self.from_url = 'http://www.xicidaili.com/nn/%d' % n
    #             result = self.verify_ip_list()
    #             results += result


s = GetProxy()
result = s.verify_ip_list()
with open('/tmp/proxy.json', 'w') as f:
    f.write(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':')))
