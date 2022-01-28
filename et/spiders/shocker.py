import scrapy
from scrapy_selenium import SeleniumRequest


class ShockSpider(scrapy.Spider):
    name = "shocker"

    def start_requests(self):
        url = "http://shockmarket.org"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        driver = response.request.meta['driver']
        driver.find_element_by_id('react-tabs-0').click()
        labels = response.css("ul li div.stats__stat-name::text").getall()
        nums = response.css("ul li div.stats__stat-number").getall()
        self.log(f"LABELS: {labels}")
        self.log(f"STATS: {nums}")
