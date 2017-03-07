# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class Headline(Item):
    title = Field()
    body = Field()


class GunosyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    subcategory = scrapy.Field()


class NewsItem(Item):
    title = Field()
    body = Field()
    time = Field()


class AxaItem(Item):
    title = Field()
    body = Field()
    div = Field()
    p = Field()
    src = Field()
    date = Field()
    content = Field()
