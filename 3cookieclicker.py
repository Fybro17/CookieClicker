# import selenium and time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# time parameters
timeout = time.time() + 60 * 5 # 5minutes
interval = 1
check = time.time() + interval

# chrome config
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-search-engine-choice-screen") # wywala search engine
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# find consest agreement
consent = driver.find_element(By.CSS_SELECTOR, value=".fc-button-label")
consent.click()

# chose lng
time.sleep(2)
lng = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
lng.click()

# find big cookie
time.sleep(2)
cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")

# loop
while True:
    cookie.click()
    if time.time() > check:
        upgrades_price = driver.find_elements(By.CSS_SELECTOR, value=".enabled .content .price") #this one gives you list of prices
        # for loop for displaying prices
        # for item in upgrades_price:
        #     print(item.text)
        upgrades = driver.find_elements(By.CSS_SELECTOR, value=".enabled") # find only enabled upgrades
        print(len(upgrades_price)) # only for a debug
        if len(upgrades_price) > 0:
            upgrades[len(upgrades)-1].click()
        check += interval # add interval seconds
    if time.time() > timeout:
        break
