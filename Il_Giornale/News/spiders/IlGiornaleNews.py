# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:38:22 2017

@author: Davide Gambocci
"""

import scrapy
from scrapy import Spider
from News.items import IlGiornaleItem


class IlGiornaleSpider(Spider):
    name = "IlGiornaleNews"
    start_urls = ['http://www.ilgiornale.it/feed.xml']

    def parse(self, response):
        links = list(set(response.xpath('//item/link/text()').extract()))
        for link in links:
            if link is not None:
                
                yield scrapy.Request(link, callback=self.parse_page_Il_Giornale)

    def parse_page_Il_Giornale(self, response):
        item = IlGiornaleItem()
        item['title'] = response.css('div.content h1::text').extract()
        item['text'] = " ".join(response.css('div.field-items p::text').extract())
        item['newspaper'] = 'Il Giornale'
        item['resume'] = response.css('div.field-items p::text').extract()[0]
        item['author'] = response.css('div.submitted a::text').extract()
        item['date'] =  response.css('div.submitted span.updated::text').extract()
        item['condivisioni'] = 'NP'
        item['tags'] = response.css('div.field a::text').extract()
        item['link'] = str(response).strip("'200><")
        yield item
