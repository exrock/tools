#!/usr/bin/env python
class ReqList(object):
    import random
    import requests
    from pyquery import PyQuery as pq
    userAgents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]
    out_title = ['国家', '类型', 'IP地址', '端口', '服务器地址', '是否匿名', '延迟', '验证日期']
    urlxici = 'http://www.xicidaili.com/nn'

    def proxy_req(self, url, headers):
        proxy_url = 'https://myhost.pw/proxy.json'
        try:
            req = self.requests.get(proxy_url, timeout=5)
            r = self.random.choice(req.json())
            proto = r['类型']
            address = r['IP地址']
            port = r['端口']
            proxies = {'http': '%s://%s:%s' % (proto, address, port), 'https': '%s://%s:%s' % (proto, address, port)}
            req = self.pq(url, headers=headers, proxies=proxies, timeout=3)
            print ('获取初始化代理地址成功')
            return req
        except:
            conti

    # 返回西刺代理抓取到的代理IP
    def xici(self):
        from_url = self.urlxici
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Host': 'www.xicidaili.com',
            'Referer': 'http://www.xicidaili.com/',
            'User-Agent': self.random.choice(self.userAgents)
        }
        result = self.proxy_req(from_url, headers)
        # tr = 0, 获取的数据第一行为标题栏,排除
        tr = 0
        item = {}
        lines = []
        for i in result.items('tr'):
            # item = {}必须在循环内重新初始化,否则函数返回的结果是:lines中的元素全都为最后一次循坏获取的
            item = {}
            if tr < 1:
                tr += 1
                continue
            else:
                # 国家
                item[self.out_title[0]] = i('td>img').attr('alt')
                # 类型
                item[self.out_title[1]] = i('td').eq(5).text()
                # IP地址
                item[self.out_title[2]] = i('td').eq(1).text()
                # 端口
                item[self.out_title[3]] = i('td').eq(2).text()
                # 服务器地址
                item[self.out_title[4]] = i('td').eq(3)('a').text()
                # 是否匿名
                item[self.out_title[5]] = i('td').eq(4).text()
                lines.append(item)
        print(lines)


s = ReqList()
res = s.proxy_req(s.urlxici, None)
print (res)
