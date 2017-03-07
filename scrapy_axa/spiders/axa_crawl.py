# coding: utf-8

from scrapy_axa.items import Headline
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AxaSpider(CrawlSpider):
    name = 'axa_crawl'
    allowed_domains = ['axa-direct.co.jp']
    start_urls = ['http://www.axa-direct.co.jp']
    rules = (Rule(LinkExtractor(allow='/auto/*'), callback='parse_topics'),)

    def parse_topics(self, response):
        """トピックスのページからタイトルと本文を抜き出す"""
        item = Headline()
        item['title'] = response.css('title ::text').extract_first()
        item['body'] = response.css('body ::text').xpath('string()').extract_first()
        yield item
