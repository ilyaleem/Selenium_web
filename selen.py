from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")

elem = driver.find_element_by_name("q")
elem.send_keys("Статьи про скунсов")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_partial_link_text('Полосатые скунсы — Википедия').click()
elem = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table/tbody/tr[2]/td/span/a/img').click()
send_keys(Keys.ESCAPE)
