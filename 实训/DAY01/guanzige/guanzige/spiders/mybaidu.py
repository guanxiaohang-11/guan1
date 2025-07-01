import scrapy


class MybaiduSpider(scrapy.Spider):
    name = "mybaidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass
