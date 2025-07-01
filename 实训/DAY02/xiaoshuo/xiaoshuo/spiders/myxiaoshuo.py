import scrapy


class MyxiaoshuoSpider(scrapy.Spider):
    name = "myxiaoshuo"
    allowed_domains = ["sfacg.com"]
    start_urls = ["https://sfacg.com"]

    def parse(self, response):
        pass
