import scrapy
import time
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShockSpider(scrapy.Spider):
    name = "shocker"

    def start_requests(self):
        super().__init__()
        url = "https://shockmarket.org/"
        yield SeleniumRequest(url=url, callback=self.parse,
                              wait_time=10,
                              wait_until=EC.element_to_be_clickable((By.ID, 'react-tabs-0')))

    def parse(self, response):
        self.log(f"META: {response.request.meta}")
        driver = response.request.meta['driver']
        self.log(f"DRIVER: {driver}")
        driver.find_element_by_id('react-tabs-0').click()
        time.sleep(1)
        labels = response.css("ul li div.stats__stat-name::text").getall()
        nums = response.css("ul li div.stats__stat-number").getall()
        self.log(f"LABELS: {labels}")
        self.log(f"STATS: {nums}")
