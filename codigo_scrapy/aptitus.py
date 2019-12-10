# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class AptitusItem(Item):
    empleo = Field()
    empresa = Field()
    ubicacion = Field()
    sueldo = Field()
    descripcion = Field()
    requisitos = Field()

class AptitusCrawler(CrawlSpider):
    name = "aptituscrawler"
    start_urls = ['https://aptitus.com/buscar-trabajo-en-peru']
    allowed_domains = ['aptitus.com']
    
    rules = (
        Rule(LinkExtractor(allow = r'page='), follow=True),
        Rule(LinkExtractor(allow = r'/ofertas-de-trabajo'), follow=True, callback='parse_items'),        
    )
    
    def parse_items(self, response):
        item = ItemLoader(AptitusItem(), response)
        item.add_xpath('empleo', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/h1/text()')
        item.add_xpath('empresa', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/div[3]/div/a/text()')
        item.add_xpath('ubicacion', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/div[3]/div/div/ul[1]/li[1]/a/text()')
        item.add_xpath('sueldo', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/div[3]/div/div/ul[1]/li[3]/span[2]/text()')
        item.add_xpath('descripcion', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div/p[2]/text()')
        item.add_xpath('requisitos', '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/text()')
        
        yield item.load_item()
