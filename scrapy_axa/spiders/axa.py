# coding: utf-8

from datetime import datetime

from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector

import scrapy
from scrapy import Spider
from tutorial.items import AxaItem


class AxaSpider(Spider):
    name = 'axa'
    allowed_domains = ['www.axa-direct.co.jp']

    def start_requests(self):
        url = "http://www.axa-direct.co.jp/"

        # コマンドラインから渡した引数は、デフォルトでSpiderのアトリビュートとして取得することができます。
        # 今回の場合、self.categoriesで引数の値を取得できます。
        # categories = getattr(self, 'categories', None)
        # if categories:
        #     url = '{0}{1}'.format(url, categories)

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # item['title'] = response.xpath('//title/text()').extract_first()
        # item['body'] = response.xpath('//div/ul/li/text()').extract()
        # item['div'] = response.xpath('//div[@id="press-release"]/ul/li').extract()
        # item['p'] = response.xpath('//p').extract()
        # item['src'] = response.css('img').xpath('@src').extract()

        # extractでstrに変換される
        # for li in response.xpath('//div[@id="press-release"]/ul/li'):
        #     item = AxaItem()
        #     item['date'] = li.xpath('//span/text()').extract()[0]
        #     item['content'] = li.xpath('//a/text()').extract()[0]
        #     yield item

        # item['date'] = response.xpath('//div[@id="press-release"]/ul/li/span/text()').extract_first()
        # item['content'] = response.xpath('//div[@id="press-release"]/ul/li/a/text()').extract_first()
        for sel in response.css("div#press-release > ul > li"):
            article = AxaItem()
            article['content'] = sel.css("a::text").extract_first()
            article['date'] = sel.css("span::text").extract_first()
            yield article

        # item['title'] = sel.xpath('//div[@id="press-release"]//ul/text()').extract()[0]
        # item['body'] = u'\n'.join(
        #     u''.join(p.xpath('.//text()').extract()) for p in sel.css('.story-body > p'))
        # item['time'] = datetime.strptime(
        #     u''.join(sel.xpath('//span[@class="story-date"]/span/text()').extract()),
        #     u'%d %B %YLast updated at %H:%M GMT')

        # yield item
