# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:38:22 2017

@author: Davide Gambocci
"""

import scrapy
from scrapy import Spider
from News.items import LaStampaItem


class LaStSpider(Spider):
    name = "LaStNews"
    start_urls = ['http://www.lastampa.it/rss.xml']

    def parse(self, response):
        links = list(set(response.xpath('//item/link/text()').extract()))
        for link in links:
            next_page = response.urljoin(link)
            yield scrapy.Request(next_page, callback=self.parse_page_La_Stampa)

    def parse_page_La_Stampa(self, response):
        item = LaStampaItem()
        item['newspaper'] = 'La Stampa'
        item['resume'] = response.css('div.ls-articoloCatenaccio::text').extract()
        item['author'] = response.css('div.ls-articoloAutore div::text').extract()
        item['title'] = response.css('div.ls-articoloTitolo h3::text').extract()
        item['date'] = response.css('div.ls-articoloDataPubblicazione::text').extract()  # al secondo posto c'è la data
        item['text'] = " ".join(response.css('div.ls-articoloTesto p::text').extract())
        item['tags'] = 'NP'
        item['link'] = str(response).strip("'200><")
        item['condivisioni'] = 'NP'

        yield item
