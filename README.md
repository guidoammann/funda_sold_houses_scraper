# funda-scraper
Scrapes the most important variables to get a better understanding of the current market. Useful when looking to buy a place in the Netherlands.

## How to use:
Step 1: make a venv and install scrapy
step 2: Go to settings.py and set your USER_AGENT. You can also set Concurrent requests and download delay according to     
        your preference.
step 3: run: if you want to run for sold homes in utrecht and for 250 pages on funda: 
                [scrapy crawl spider_sold_houses -o Utrecht_sold_houses.csv].
             if you want to run for a different city and different amount of pages (to test)
             you can alter the variables with -a. e.g:
                [scrapy crawl spider_sold_houses -a place=amsterdam -a page_numbers=5 -o Utrecht_sold_houses.csv]



## Scraped variables
Scraped variables are: 
    - url 
    - title 
    - postal_code 
    - neighborhood 
    - Oppervlakte 
    - price 
    - prijs_m2 
    - Soort_appartement 
    - Laatste_vraagpijs 
    - Aangeboden_sinds 
    - Soort_bouw
    - Status 
    - Inhoud 
    - Bouwjaar 
    - Aantal_kamers 
    - Aantal_badkamers 
    - Aantal_woonlagen 
    - Verkoopdatum 
    - Looptijd 
    - Gebouwgebonden_buitenruimte 
    - Externe_bergruimte 
    - Energielabel 
    - Isolatie 
    - Verwarming 
    - Warm_water 
    - Eigendomssituatie 
    - Ligging 
    - Balkon_dakterras 
    - Schuur_berging 
    - Bijdrage_VvE 
    - Soort_parkeergelegenheid 

