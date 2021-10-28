# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrpeItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    features = scrapy.Field()
    price = scrapy.Field()
    type = scrapy.Field()
