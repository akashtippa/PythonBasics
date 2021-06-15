import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Act = ActionChains(driver)
Act.move_to_element(driver.find_element_by_id("mousehover")).perform()

driver.find_element_by_link_text("Top").click()

# Act.move_to_element(driver.find_element_by_id("mousehover")).perform()

# driver.find_element_by_link_text("Reload").click()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
time.sleep(2)
Act.double_click(driver.find_element_by_id("double-click")).perform()

time.sleep(3)
alert = driver.switch_to.alert
alert.accept()