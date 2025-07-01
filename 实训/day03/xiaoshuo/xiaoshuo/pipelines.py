# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def open_spider(self, spider):
    self.items = open("xioashuo.csv", 'a', encoding='utf-8')

class XiaoshuoPipeline:
    def process_item(self, item, spider):
        self.file.write(f"{item['bname']},{item['author']},{item['renqi']},{item['zishu']},{item['tupian']}\n")
        return item
def close_spider(self, spider):
    self.file.close()