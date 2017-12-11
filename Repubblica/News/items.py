
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RepubblicaItem(scrapy.Item):
    newspaper = Field()
    title = Field()
    resume = Field()
    date = Field()
    author = Field()
    tags = Field()
    text = Field()
    link = Field()
    condivisioni= Field()
    
