# -*- coding: utf-8 -*-
import json
import base64
import random
import time

import requests
import logging
from scrapy import signals
from twisted.internet.error import TimeoutError

LOG = logging.getLogger(__name__)

NETWORK_STATUS = True
PROXY_STATUS = True


class EmploymentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class EmploymentDownloaderMiddleware(object):
    pass
# class EmploymentDownloaderMiddleware(object):
#
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     def __init__(self, PROXY_IP, PROXY_LIST, PROXY_USER, PROXY_PASS):
#         self.PROXY_IP = PROXY_IP
#         self.PROXY_LIST = PROXY_LIST
#         self.PROXY_USER = PROXY_USER
#         self.PROXY_PASS = PROXY_PASS
#
#         # 添加白名单
#         ip = self.proxy_request("http://soft.data5u.com/wl/myip/364b34f504a96d09d677bed1b3bc6d8a.html").text
#         time.sleep(5)
#         ip_list = self.proxy_request(
#             "http://soft.data5u.com/wl/mywhitelist/364b34f504a96d09d677bed1b3bc6d8a.html").text
#         if ip not in ip_list:
#             time.sleep(5)
#             append_ip = self.proxy_request(
#                 "http://soft.data5u.com/wl/setip/364b34f504a96d09d677bed1b3bc6d8a.html?ips=&clear=").text
#             time.sleep(300)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             PROXY_IP=crawler.settings.get("PROXY_IP"),
#             PROXY_LIST=crawler.settings.get("PROXY_LIST"),
#             PROXY_USER=crawler.settings.get("PROXY_USER"),
#             PROXY_PASS=crawler.settings.get("PROXY_PASS"),
#         )
#
#     def process_request(self, request, spider):
#         global NETWORK_STATUS, PROXY_STATUS
#         if NETWORK_STATUS and self.PROXY_IP:
#             # proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((self.PROXY_USER + ":" + self.PROXY_PASS), "ascii")).decode("utf8")
#
#             for i in range(1, 6):
#                 # 设置代理
#                 try:
#                     res = self.proxy_request(self.PROXY_IP).text
#                     # proxy_dict = json.loads(res)
#                     # data = proxy_dict['data'][0]
#                     request.meta["proxy"] = "https://" + res
#                     # request.meta["proxy"] = self.PROXY_IP
#                     # request.headers["Proxy-Authorization"] = proxyAuth
#                     break
#                 except requests.exceptions.Timeout:
#                     '''请求超时'''
#                     LOG.warning('请求超时，第%s次重复请求' % i)
#                     continue
#                 except Exception:
#                     LOG.warning("PROXY_IP配置异常, 开始使用PROXY_LIST代理")
#                     NETWORK_STATUS = False
#                     break
#         elif self.PROXY_LIST and isinstance(self.PROXY_LIST, list) and PROXY_STATUS is True:
#             request.meta["proxy"] = "http://" + random.choice(self.PROXY_LIST)
#         elif PROXY_STATUS:
#             PROXY_STATUS = False
#             LOG.warning("无法获取代理, 开始使用无代理请求")
#
#     def proxy_request(self, url):
#         response = requests.get(url, timeout=5)
#         if response.status_code == 200:
#             return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         if isinstance(exception, TimeoutError):
#             return request
