# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:38:22 2017

@author: Davide Gambocci
"""

import scrapy
from scrapy import Spider
from News.items import IlCorriereItem


class IlCorrSpider(Spider):
    name = "IlCorrNews"
    start_urls = ['http://xml.corriereobjects.it/rss/homepage.xml']

    def parse(self, response):
        links = list(set(response.xpath('//item/link/text()').extract()))
        for link in links:
            if link is not None:
                yield scrapy.Request(link, callback=self.parse_page_Il_Corriere)

    def parse_page_Il_Corriere(self, response):
        item = IlCorriereItem()
        item['title'] = response.css('header h1::text').extract()
        item['text'] = " ".join(response.css('div.chapter p::text').extract())
        item['newspaper'] = 'Il Corriere della Sera'
        item['resume'] = response.css('header h2::text').extract()
        item['author'] = 'NP'
        item['date'] = response.css(' div.article-date-place::text').extract()
        item['condivisioni'] = 'NP'
        item['tags'] = 'NP'
        item['link'] = str(response).strip("'200><")
        yield item
