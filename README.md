helloscrapy
===========

Scrapy example spiders.

An example to save into MongoDB is available in the `mongo` branch.

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
scrapy crawl bbc # an example of SitemapSpider
scrapy crawl cnet # an example of CrawlSpider
```

See (Japanese)
--------------

http://orangain.hatenablog.com/entry/scrapy
