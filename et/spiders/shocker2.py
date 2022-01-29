import scrapy
import time
# from scrapy_selenium import SeleniumRequest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ShockSpider(scrapy.Spider):
    name = "shocker2"

    def start_requests(self):
        super().__init__()
        url = "https://shockmarket.org/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        driver = webdriver.Chrome()
        # self.log(f"DRIVER: {driver}")
        driver.get(response.url)
        time.sleep(2)
        driver.find_element_by_id('react-tabs-0').click()
        time.sleep(5)
        sel = scrapy.Selector(text=driver.page_source)
        labels = sel.css("ul.stats__list li.stats__stat div.stats__stat-name::text").getall()
        nums = sel.css("ul.stats__list li.stats__stat div.stats__stat-number").getall()
        self.log(f"LABELS: {labels}")
        self.log(f"STATS: {nums}")
