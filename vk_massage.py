from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.vk.com")

elem = driver.find_element_by_id("index_email")
elem.send_keys("example@mail.ru")

elem = driver.find_element_by_id("index_pass")
elem.send_keys("examplepass")

elem = driver.find_element_by_id("index_login_button").click()

time.sleep(15)

elem = driver.find_element_by_link_text("Сообщения").click()

time.sleep(4)

elem = driver.find_element_by_xpath('//*[@id="im_dialogs"]/div[1]/div[1]/div/div[1]/li[2]/div[2]/div').click()
elem = driver.find_element_by_id("im_editable0")
elem.send_keys("Пример сообщения")
elem.send_keys(Keys.RETURN)
