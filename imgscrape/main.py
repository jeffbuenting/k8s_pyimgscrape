# Docker Container -  https://shinesolutions.com/2018/09/13/running-a-web-crawler-in-a-docker-container/

import json
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

from pyimgscrape.spiders.imgscrape import ImgscrapeSpider

# call spider and return items : https://github.com/scrapy/scrapy/issues/3856
def spider_results(url=None):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)  

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    # running crawler from script: https://docs.scrapy.org/en/latest/topics/practices.html 
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImgscrapeSpider, url=SearchUrl)
    process.start()
    return results


SearchUrl = 'https://nextdoornikki.com/hosted/gal/watermellon/1581254'

if __name__ == '__main__':
    results = []
    for item in spider_results(SearchUrl):
        results.append(item['img'])

    print(results)