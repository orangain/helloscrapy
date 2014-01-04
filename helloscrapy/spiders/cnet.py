# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from helloscrapy.items import NewsItem


class CNetSpider(CrawlSpider):
    name = 'cnet'
    allowed_domains = ['news.cnet.com']
    start_urls = [
        'http://news.cnet.com/8324-12_3-0.html',
    ]
    rules = [
        # 正規表現 'begin=201312' にマッチするリンクを辿る
        Rule(SgmlLinkExtractor(allow=(r'begin=201312', ), restrict_xpaths=('/html', ))),
        # 正規表現 '/[\d_-]+/[^/]+/$' にマッチするリンクをparse_newsメソッドでパースする
        Rule(SgmlLinkExtractor(allow=(r'/[\d_-]+/[^/]+/$', ), restrict_xpaths=('/html', )),
             callback='parse_news'),
    ]

    def parse_news(self, response):
        item = NewsItem()

        sel = Selector(response)
        item['title'] = sel.xpath('//h1/text()').extract()[0]
        item['body'] = u'\n'.join(
            u''.join(p.xpath('.//text()').extract()) for p in sel.css('#contentBody .postBody p'))
        item['time'] = datetime.strptime(
            sel.xpath('//time[@class="datestamp"]/text()').extract()[0].strip()[:-4],
            u'%B %d, %Y %I:%M %p')

        yield item
