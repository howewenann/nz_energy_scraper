# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NzEnergyScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



from scrapy.item import Item, Field

class FiledownloadItem(Item):
    file_urls = Field()
    files = Field()