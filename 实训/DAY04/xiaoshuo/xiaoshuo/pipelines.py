# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from typing import Any

from scrapy import Request
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.media import MediaPipeline

class XiaoshuoPipeline:
    # 爬虫程序执行之前自动调用
    def open_spider(self, spider):
        self.file = open("xiaoshuo.csv", "a", encoding="utf-8")
    # item接受引擎返回的数据
    def process_item(self, item, spider):
        # 处理数据，保存数据
        self.file.write(f"{item['bname']},{item['author']},{item['renqi']},{item['zishu']},{item['tupian']}\n")
        return item
    #爬虫程序结束自动调用
    def close_spider(self, spider):
        self.file.close()
class ImagesPipeline2(ImagesPipeline):
    def get_media_requests(self, item, info):
        # print(item)
        tupian=item['tupian']
        print(tupian)
        yield Request(tupian,meta={"src":tupian})
    def file_path(
        self,
        request=None,
        response = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None):
        src=request.meta["src"]
        # print(src)
        src=src.split("/")[-1]
        print("===",src)
        return f"A/{src}"