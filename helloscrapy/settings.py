# Scrapy settings for helloscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'helloscrapy'

SPIDER_MODULES = ['helloscrapy.spiders']
NEWSPIDER_MODULE = 'helloscrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'helloscrapy (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 3
ROBOTSTXT_OBEY = True
