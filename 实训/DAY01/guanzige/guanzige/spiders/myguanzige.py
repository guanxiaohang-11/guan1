import scrapy


class MyguanzigeSpider(scrapy.Spider):
    name = "myguanzige"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass
