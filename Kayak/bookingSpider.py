import pandas as pd
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess, signals
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
import logging

## code pour accéder à mes fichiers sous collab
colab = True
colab = False
mypath = ''
## détermination du path
if colab:
    from sys import path
    from google.colab import drive
    drive.mount('/content/drive')
    path.insert(0,'/content/drive/MyDrive/Getaround/')
    mypath = path[0]

## get a list of towns from csv file
towns = pd.read_csv(f'{mypath}src/towns.csv')['ville'].to_list()      

class BookingSpider(scrapy.Spider):
    name = 'BookingSpider'
    allowed_domains = ['www.booking.com']
       
    ## a list comprehension iterating in towns list to provide urls each with the name of the town to search    
    start_urls = [f'https://www.booking.com/searchresults.fr.html?ss={town}' for town in towns]
    
    def parse( self, response):
        ville = response.xpath('//div[@id="right"]/div/div/div/div/h1/text()')
        distances =response.xpath('//span[@data-testid="distance"]/text()')
        urls = response.xpath('//h3/a[@data-testid="title-link"]/@href')
        for url,distance in zip(urls,distances):
            yield response.follow(url=url.get(), callback = self.parse2, \
                    meta={'ville': ville, 'distance':distance, 'url':url})
        
    def parse2(self, response):
        yield {
            "ville": response.request.meta['ville'].get().split(':')[0].strip(),
            "hotel": response.xpath('//h2[@class="d2fee87262 pp-header__title"]/text()').get().strip(),
            "url": response.request.meta['url'].get().strip(),
            "distance": response.request.meta['distance'].get().strip(),
            "adresse": response.xpath('//p[@id="showMap2"]/span[@data-node_tt_id="location_score_tooltip"]/text()').get().strip(),
            "coordinates": response.xpath('//p[@id="showMap2"]/a[@id="hotel_address"]/@data-atlas-bbox').get().strip(),
            "score": response.xpath('//div[@class="b5cd09854e d10a6220b4"]/text()').get(),
            "description": response.xpath('//div[@id="property_description_content"]//p/text()').get().strip()
        }

        
## Name of the file where the results will be saved
filename = "towns_scraped.json"

## If file already exists, delete it before crawling
if filename in os.listdir(f'{mypath}src/'):
        os.remove(f'{mypath}src/' + filename)

## Declare a new CrawlerProcess with some settings
process = CrawlerProcess(settings = {
    ## USER_AGENT => Simulates a browser on an OS
    'USER_AGENT': 'Mozilla Firefox/105.0.1',
    ## FEED_EXPORT_ENCODING': 'utf-8' => avoid unwanted characters
    'FEED_EXPORT_ENCODING' : 'utf-8',
    "AUTOTHROTTLE_ENABLED": True,
    ## LOG_LEVEL => Minimal Level of Log
    'LOG_LEVEL': logging.INFO,
    ## FEEDS => Where the file will be stored
    "FEEDS": {
        f'{mypath}src/' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider defined above
process.crawl(BookingSpider)
process.start()
