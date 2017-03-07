# coding: utf-8

from scrapy.spiders import SitemapSpider


class AxaSpider(SitemapSpider):
    name = 'axa_sitemap'
    allowed_domains = ['axa-direct.co.jp']

    # robots.txtを指定すると、SitemapディレクティブからXMLサイトマップのURLを取得する
    sitemap_urls = [
        'http://www.axa-direct.co.jp/robots.txt'
    ]

    # サイトマップインデックスからたどるサイトマップURLの正規表現のリスト
    sitemap_follow = [
        r'auto'
    ]

    sitemap_rules = [(r'/auto/service', 'parse_topic'), ]

    def parse_topic(self, response):
        yield {
            'title': response.css('title::text').extract_first(),
            'url': response.url,
        }

    # sitemap_rulesを指定しない場合全てのURLに対するコールバック関数はparseメソッドになる
    def parse(self, response):
        return
