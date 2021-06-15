import time
from _ast import arguments

import document as document
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.implicitly_wait(6)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a
for product in products:
    ProductName = product.find_element_by_xpath("div/h4/a").text
    if ProductName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

driver.find_element_by_xpath("//button[normalize-space()='Checkout']").click()
driver.find_element_by_id("country").send_keys("Ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
driver.find_element_by_xpath("//input[@value='Purchase']").click()
SuccessMessage = driver.find_element_by_class_name("alert-success").text
assert "Success!" in SuccessMessage

driver.get_screenshot_as_file("screenshot.png")
time.sleep(2)
driver.close()
