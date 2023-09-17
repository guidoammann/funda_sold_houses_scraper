import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from funda.items import FundaItems


class FundaSoldSpider(scrapy.Spider):
    name = "spider_sold_houses"
    allowed_domains = ["funda.nl"]

    def __init__(self, place="utrecht", page_numbers=250):
        self.page_numbers = int(page_numbers)
        self.start_urls = [
            f"https://www.funda.nl/zoeken/koop?selected_area=%5B%22{place}%22%5D&availability=%5B%22unavailable%22%5D&search_result={page_number}"
            for page_number in range(1, self.page_numbers)
        ]
        self.base_url = f"https://www.funda.nl/koop/{place}/"
        self.le1 = LinkExtractor(allow=r"%s+(huis|appartement)-\d{8}" % self.base_url)

    def parse(self, response):
        links = self.le1.extract_links(response)

        for link in links:
            item = FundaItems()
            item["url"] = link.url
            yield scrapy.Request(link.url, callback=self.get_items, meta={"item": item})

    def get_items(self, response):
        new_item = response.request.meta["item"]
        title = response.xpath("//title/text()").extract()[0]
        postal_code = re.search(r"\d{4} [A-Z]{2}", title).group(0)
        neighborhood = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/header/div/div/div[2]/div[1]/h1/span[2]/a/text()'
        ).get()
        Oppervlakte = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/header/div/div/div[2]/div[1]/section/ul/li[1]/span[2]/text()'
        ).get()
        price = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/header/div/div/div[3]/div/strong/text()'
        ).get()
        prijs_m2 = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[1]/dd[2]/text()'
        ).get()
        Soort_appartement = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[2]/dd[1]/span/text()'
        ).get()
        Laatste_vraagpijs = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[1]/dd[1]/span[1]/text()'
        ).get()
        Aangeboden_sinds = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[1]/div/dl/dd[1]/text()'
        ).get()
        Soort_bouw = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[2]/dd[2]/span/text()'
        ).get()
        Status = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[1]/dd[3]/span/text()'
        ).get()
        Inhoud = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[3]/dd[3]/span/text()'
        ).get()
        Bouwjaar = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[2]/dd[3]/span[1]/text()'
        ).get()
        Aantal_kamers = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[4]/dd[1]/span/text()'
        ).get()
        Aantal_badkamers = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[4]/dd[2]/span/text()'
        ).get()
        Aantal_woonlagen = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[4]/dd[3]/span/text()'
        ).get()
        Verkoopdatum = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[1]/div/dl/dd[2]/text()'
        ).get()
        Looptijd = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[1]/div/dl/dd[3]/text()'
        ).get()
        Gebouwgebonden_buitenruimte = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[3]/dd[2]/dl/dd[2]/span/text()'
        ).get()
        Externe_bergruimte = response.xpath(
            '//*[@id="content"]/div[2]/div[2]/div[1]/section[4]/div/dl[3]/dd[2]/dl/dd[3]/span/text()'
        ).get()
        Energielabel = response.xpath(
            '//*[@id="content"]/div[2]/div[2]/div[1]/section[4]/div/dl[5]/dd[1]/span/text()'
        ).get()
        Isolatie = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[5]/dd[2]/span/text()'
        ).get()
        Verwarming = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[5]/dd[3]/span/text()'
        ).get()
        Warm_water = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[5]/dd[4]/span/text()'
        ).get()
        Eigendomssituatie = response.xpath(
            '//*[@id="content"]/div[2]/div[2]/div[1]/section[4]/div/dl[6]/dd[2]/dl/dd[1]/span/text()'
        ).get()
        Ligging = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[6]/dd[1]/span/text()'
        ).get()
        Balkon_dakterras = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[6]/dd[2]/span/text()'
        ).get()
        Schuur_berging = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[7]/dd/span/text()'
        ).get()
        Bijdrage_VvE = response.xpath(
            '//*[@id="content"]/div[2]/div[2]/div[1]/section[4]/div/dl[1]/dd[6]/span/text()'
        ).get()
        Soort_parkeergelegenheid = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/section[5]/div/dl[8]/dd/span/text()'
        ).get()

        new_item["title"] = title
        new_item["postal_code"] = postal_code
        new_item["neighborhood"] = neighborhood
        new_item["Oppervlakte"] = Oppervlakte
        new_item["price"] = price
        new_item["prijs_m2"] = prijs_m2
        new_item["Soort_appartement"] = Soort_appartement
        new_item["Laatste_vraagpijs"] = Laatste_vraagpijs
        new_item["Aangeboden_sinds"] = Aangeboden_sinds
        new_item["Soort_bouw"] = Soort_bouw
        new_item["Status"] = Status
        new_item["Inhoud"] = Inhoud
        new_item["Bouwjaar"] = Bouwjaar
        new_item["Aantal_kamers"] = Aantal_kamers
        new_item["Aantal_badkamers"] = Aantal_badkamers
        new_item["Aantal_woonlagen"] = Aantal_woonlagen
        new_item["Verkoopdatum"] = Verkoopdatum
        new_item["Looptijd"] = Looptijd
        new_item["Gebouwgebonden_buitenruimte"] = Gebouwgebonden_buitenruimte
        new_item["Externe_bergruimte"] = Externe_bergruimte
        new_item["Energielabel"] = Energielabel
        new_item["Isolatie"] = Isolatie
        new_item["Verwarming"] = Verwarming
        new_item["Warm_water"] = Warm_water
        new_item["Eigendomssituatie"] = Eigendomssituatie
        new_item["Ligging"] = Ligging
        new_item["Balkon_dakterras"] = Balkon_dakterras
        new_item["Schuur_berging"] = Schuur_berging
        new_item["Bijdrage_VvE"] = Bijdrage_VvE
        new_item["Soort_parkeergelegenheid"] = Soort_parkeergelegenheid

        yield new_item
