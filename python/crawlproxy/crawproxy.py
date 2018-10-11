#!/usr/bin/env python3
# 抓取高匿代理
import json
from pyquery import PyQuery as pq
class CrawlProxy():
    userAgents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]
    outputTitle = ['国家', '类型', 'IP地址', '端口', '服务器地址', '是否匿名', '延迟', '验证日期']
    def xici(self):

    def verify_ip(self, arg1, arg2, arg3):
        import random
        import requests
        verify_url = 'http://httpbin.org/ip'
        proxies = {'http': '%s://%s:%s' % (arg1, arg2, arg3), 'https': '%s://%s:%s' % (arg1, arg2, arg3)}
        headers = {'User-Agent': random.choice(self.userAgents)}
        try:
            req = requests.get(verify_url, proxies=proxies, headers=headers, timeout=3)
            timeout = ('%.2f秒' % (req.elapsed.microseconds / 10 ** 6))
            return timeout
        except:
            pass


    def sort_list(self):

    def ip_counts(self):
        if count < 2000:
            self.append_valid()
        else:
            self.check_list()

    def append_valid(self):
        self.get_proxy_list()
        self.deduplication_ip()
        self.verify_ip(type, ip, port)
        self.append_ip()
        self.ip_counts()

    def get_proxy_list(self):

    def deduplication_ip(self):

    def append_ip(self):

    def check_list(self):
        self.verify_ip(type, ip, port)
        self.sort_list()
        self.ip_counts()



while True:
    CrawlProxy().check_list()