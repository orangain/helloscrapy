helloscrapy
===========

Sample spiders

Requirements
------------

- Python 2.7
- Virtualenv
- libxml2-dev & libxslt-dev

Setup
-----

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Usage
-----

```
scrapy crawl bbc # a sample of SitemapSpider
scrapy crawl cnet # a sample of CrawlSpider
```
