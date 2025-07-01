import scrapy


class NewlianghaoSpider(scrapy.Spider):
    name = "newlianghao"
    allowed_domains = ["jihaoba.com"]
    start_urls = ["https://jihaoba.com/escrow"]

    def parse(self, response):
        print(response.text)
        #lists=response.xpath("//div[@class='escrow-right']/div[@class='list']/div[@class='numbershow']/ul")
        #print(lists)
        #for li in lists:
            #手机号
            #haoma=li.xpath(".//li[@class='number hmzt']/a/text()").extract_first()
            #print(haoma)
