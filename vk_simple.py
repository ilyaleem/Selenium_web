from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.vk.com")

elem = driver.find_element_by_id("index_email")
elem.send_keys("example@mail.ru")

elem = driver.find_element_by_id("index_pass")
elem.send_keys("example_pass")

elem = driver.find_element_by_id("index_login_button").click()

time.sleep(22)

elem = driver.find_element_by_id('post_field')
elem.send_keys("Этот текст набрала и опубликовала моя программа, которую я написал в Python")

elem = driver.find_element_by_id("send_post").click()