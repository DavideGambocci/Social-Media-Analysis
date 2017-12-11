# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:38:22 2017

@author: Davide Gambocci
"""

import scrapy
from scrapy import Spider
from News.items import RepubblicaItem


class RepSpider(Spider):
    name = "RepNews"
    start_urls = ['http://www.repubblica.it/rss/homepage/rss2.0.xml']

    def parse(self, response):
        links = list(set(response.xpath('//item/link/text()').extract()))
        for link in links:
            yield scrapy.Request(link, callback=self.parse_page_Repubblica)


    def parse_page_Repubblica(self, response):
        item = RepubblicaItem()
        item['newspaper'] = 'La Repubblica'
        item['title'] = response.css('div.inner-container header h1::text').extract()
        item['resume'] = response.css('div.inner-container p::text').extract()
        item['date'] = response.css('div.main-content time::attr(content)').extract()
        item['author'] = 'NP'
        item['condivisioni'] = 'NP'
        item['tags'] = response.css('div.body-text dd a::text').extract()
        item['text'] = " ".join(response.css('div.body-text span::text').extract())
        item['link'] = str(response).strip("'200><")
        yield item
