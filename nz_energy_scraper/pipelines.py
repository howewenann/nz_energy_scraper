# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NzEnergyScraperPipeline(object):
    def process_item(self, item, spider):
        return item


# Custom file pipeline to keep original names
import os
from urllib.parse import urlparse
from scrapy.pipelines.files import FilesPipeline

class CustomFilesPipeline(FilesPipeline):

	def file_path(self, request, response=None, info=None):
		return request.url.split('/')[-1]