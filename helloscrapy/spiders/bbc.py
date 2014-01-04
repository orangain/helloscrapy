# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector

from helloscrapy.items import NewsItem


class BBCSpider(SitemapSpider):
    name = 'bbc'
    allowed_domains = ['www.bbc.co.uk']
    sitemap_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://www.bbc.co.uk/news/sitemap.xml',
    ]
    sitemap_rules = [
        # 正規表現 '/news/' にマッチするページをparse_newsメソッドでパースする
        (r'/news/', 'parse_news'),
    ]

    def parse_news(self, response):
        item = NewsItem()

        sel = Selector(response)
        item['title'] = sel.xpath('//h1[@class="story-header"]/text()').extract()[0]
        item['body'] = u'\n'.join(
            u''.join(p.xpath('.//text()').extract()) for p in sel.css('.story-body > p'))
        item['time'] = datetime.strptime(
            u''.join(sel.xpath('//span[@class="story-date"]/span/text()').extract()),
            u'%d %B %YLast updated at %H:%M GMT')

        yield item
