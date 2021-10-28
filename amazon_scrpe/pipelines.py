# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class AmazonScrpePipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://akash:8jNYW8eVQCHORH6M@cluster0.k8zrx.mongodb.net/product?retryWrites=true&w=majority")

        # creating database
        db = self.conn['amazon_db']
        # creating collection
        self.collection = db['products']
        
        
    def process_item(self, item, spider):
        pass
        self.collection.insert(dict({
            'title': item['title'],
            'image': item['image'],
            'price': item['price'],
            'features': item['features'],
            'type': item['type']
        }))
        return item
