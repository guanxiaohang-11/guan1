import scrapy


class NewxiaoshuoSpider(scrapy.Spider):
    name = "newxiaoshuo"
    allowed_domains = ["sfacg.com"]
    start_urls = ["https://book.sfacg.com"]

    def parse(self, response):
        #print(response.text)
        li_list=response.xpath("//div[@class='container']/div[@class='column'][2]//ul[@class='story-list']/li")
        #print(li_list)
        for li in li_list:
            #书名
            bname=li.xpath("./p[@class='title']/a/text()").extract_first()
            #print(bname)
            #作者
            author=li.xpath(".//div[@class='info-layer']//div[@class='author-info']/span[2]/text()").extract_first()
            #print(author)
            #人气
            renqi=li.xpath(".//div[@class='info-layer']//div[@class='book-info']/p[2]/span/text()").extract_first()
            #print(renqi)
            #字数
            zishu=li.xpath(".//div[@class='info-layer']//div[@class='book-info']/p[1]/span/text()").extract_first()
            #print(zishu)
            #图片链接
            tupian=li.xpath(".//div[@class='pic']//img/@src").extract_first()
            # print(tupian)
            yield {
                "bname":bname,
                "author":author,
                "renqi":renqi,
                "zishu":zishu,
                "tupian":tupian,
            }
