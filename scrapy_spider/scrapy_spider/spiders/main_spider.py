# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request

class MainSpider(scrapy.Spider):
    name = "ramboo"
    def __init__(self, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]



    def parse(self, response):
        # print(response.body.decode("utf-8"))
        print(response.text)
        print(response.xpath('/html/body/div[3]/div[1]/div[2]').extract())
        yield Request("http://service.cpd.com.cn/n209739/index.html", callback=self.get_community)

    def get_community(self, response):
        print(response.xpath('//*[@id="newslist"]/ul[1]/li[1]/a').extract())
