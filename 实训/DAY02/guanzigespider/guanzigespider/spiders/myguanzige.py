import scrapy


class MyguanzigeSpider(scrapy.Spider):
    name = "myguanzige"
    #允许被爬取的网站域名
    allowed_domains = ["baidu.com"]
    #第一个爬取的网页域名URL
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        # response
        # 解析响应内容
        print(response.text)