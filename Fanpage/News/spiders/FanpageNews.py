# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:38:22 2017

@author: Davide Gambocci
"""

import scrapy
from scrapy import Spider
from News.items import FanpageItem


class FanpageSpider(Spider):
    name = "FanpageNews"
    start_urls = ['http://www.fanpage.it/feed/']

    def parse(self, response):
        links = list(set(response.xpath('//item/link/text()').extract()))
        for link in links:
            if link is not None:
                yield scrapy.Request(link, callback=self.parse_page_Fanpage)

    def parse_page_Fanpage(self, response):
        item = FanpageItem()
        item['title'] = response.css('div.art-title h1::text').extract()
        item['text'] = " ".join(response.css('div.box-general p::text').extract())
        item['newspaper'] = 'Fanpage'
        item['resume'] = response.css('div.art-subtitle::text').extract()
        item['author'] = response.css('div.art-autor span::text').extract()
        item['date'] = response.css('div.art-date span::text').extract()
        item['condivisioni'] =  'NP'
        item['tags'] = 'NP'
        item['link'] = str(response).strip("'200><")
        yield item
