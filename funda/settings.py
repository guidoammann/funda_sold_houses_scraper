# -*- coding: utf-8 -*-

# Scrapy settings for funda project


BOT_NAME = "funda"

SPIDER_MODULES = ["funda.spiders"]
NEWSPIDER_MODULE = "funda.spiders"


# Add your user agent here!
USER_AGENT = ""


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16): set to 2 to avoid getting banned
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0): set to 1 to avoid getting banned
DOWNLOAD_DELAY = 1
