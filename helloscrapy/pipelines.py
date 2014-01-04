# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class MongoPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        return cls(
            settings.get('MONGO_URL', 'mongodb://localhost:27017/'),
            settings.get('MONGO_DATABASE', 'scrapy'),
        )

    def __init__(self, mongo_url, mongo_database):
        client = pymongo.MongoClient(mongo_url)
        self.db = client[mongo_database]

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.save(dict(item))
        return item
