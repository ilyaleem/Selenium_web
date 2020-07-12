from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://freebitco.in")

btc = driver.find_element_by_id("signup_form_email")
btc.send_keys('example@gmail.com')

btc = driver.find_element_by_id('signup_form_password')
btc.send_keys('examplepass')

time.sleep(9)

btc = driver.find_element_by_link_text('Got it!').click()

time.sleep(30)

btc = driver.find_element_by_css_selector('#push_notification_modal > div.push_notification_big > div:nth-child(2) > div > div.pushpad_deny_button').click()

while True:
    btc = driver.find_element_by_id("free_play_form_button").click()
    time.sleep(8)
    btc = driver.find_element_by_css_selector('#myModal22 > a').click()
    time.sleep(3660)
   