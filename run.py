from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapylianjia.spiders.lianjia import LianjiaSpider

settings = get_project_settings()
process =CrawlerProcess(settings=settings)


process.crawl(LianjiaSpider)
process.start()
