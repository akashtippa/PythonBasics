import time
from _ast import arguments

import document as document
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("TestMe")
# print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
time.sleep(2)
driver.find_element_by_link_text("Shop").click()

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


