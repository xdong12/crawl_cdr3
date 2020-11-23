#!/usr/bin/env python3
# coding: utf-8
# Time: 2020/11/20 16:20
# Author: xd

"""
http://www.chinadegrees.cn/webrms/pages/Ranking/xkpmGXZJ.jsp
"""

import re
import scrapy
from employment.settings import HEADERS


class DslxkpgSpider(scrapy.Spider):
    """第三轮学科评估"""
    name = 'xkpg3'
    allowed_domains = ['edu.cn']
    # start_urls可以设置多个
    start_urls = ['http://www.chinadegrees.cn/webrms/pages/Ranking/xkpmGXZJ.jsp']


    # redis_key = 'ranking:start_urls'  # redis_key,用于在redis 添加起始url
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": HEADERS
    }

    def parse(self, response):
        xk_xpath = response.xpath('//*[@id="pbg0"]/table/tr/td[1]/p')
        for x in xk_xpath:
            suffix = x.xpath('./a/@href').extract_first()
            xk = x.xpath('./a/text()').extract_first().replace(' ','')
            new_url = 'http://www.cdgdc.edu.cn/webrms/pages/Ranking/' + suffix
            yield scrapy.Request(url=new_url, meta={'item':{'学科门类': xk}}, callback=self.parse_yjxk)

    def parse_yjxk(self, response):
        yjxk_xpath = response.xpath('//*[@id="leftgundong"]/table/tr/td/p')
        item = response.meta.get('item')

        for y in yjxk_xpath:
            suffix = y.xpath('./a/@href').extract_first()
            yjxk_text = y.xpath('./a/text()').extract_first()
            yjxk = re.search('[\u4e00-\u9fa5]+', yjxk_text).group(0)
            xkdm = re.search('[0-9]+', yjxk_text).group(0)
            item['学科'] = yjxk
            item['学科代码'] = xkdm
            new_url = 'http://www.cdgdc.edu.cn/webrms/pages/Ranking/' + suffix
            yield scrapy.Request(url=new_url, meta={'item': item}, callback=self.parse_table)

    def parse_table(self,response):
        tr_xpath = response.xpath('//*[@id="pbg0"]/table/tr/td[3]/table/tr[4]/td/div/table/tr')
        url = response.url
        item = response.meta.get('item')
        for tr in tr_xpath:
            td = tr.xpath('./td')
            if len(td)>1:
                score = td[1].xpath('./text()').extract_first()
                xx_text = td[0].xpath('./div/text()').extract_first()
            else:
                xx_text = td[0].xpath('./div/text()').extract_first()

            xxmc = re.search('[\u4e00-\u9fa5]+', xx_text).group(0)
            xxdm = re.search('[0-9]+', xx_text).group(0)
            item['评估结果'] = score
            item['学校代码'] = xxdm
            item['学校名称'] = xxmc
            item['来源'] = '第三轮学科评估'
            item['url'] = url
            yield item


