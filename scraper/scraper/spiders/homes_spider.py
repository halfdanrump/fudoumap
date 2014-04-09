from scrapy.contrib.spiders import CrawlSpider

class HomesSpider(CrawlSpider):
	name = homes
	allowed_domains = ['homes.co.jp']
	start_urls = ['http://www.homes.co.jp/mansion/tokyo/line/']

