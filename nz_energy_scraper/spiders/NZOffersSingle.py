# -*- coding: utf-8 -*-
import scrapy
from nz_energy_scraper.items import FiledownloadItem

class NzofferssingleSpider(scrapy.Spider):
    name = 'NZOffersSingle'
    allowed_domains = ['www.emi.ea.govt.nz/Wholesale/Datasets/BidsAndOffers/Offers/2019']
    start_urls = ['http://www.emi.ea.govt.nz/Wholesale/Datasets/BidsAndOffers/Offers/2019/']

    def parse(self, response):

    	for link in [response.xpath('//following::tr[1]/td[1]/a[contains(@href, "csv")]')[0]]:
	    	relative_url = link.xpath('.//@href').extract_first()
	    	absolute_url = response.urljoin(relative_url)
	    	yield FiledownloadItem(file_urls = [absolute_url])
