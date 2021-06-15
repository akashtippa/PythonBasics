import time

from selenium import webdriver
# Implicit waits
# Explicit waits
# pause the test for seconds using time class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(4)
# valaidate products counts
ProdCount = len(driver.find_elements_by_css_selector("div[class='product']"))
print(ProdCount)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
# Items = driver.find_elements_by_xpath("//div[@class='cart-preview active']//div//div//p[@class='product-name']")

# print(Items.text)

driver.find_element_by_css_selector("div[class='cart-preview active'] button[type='button']").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span[class='promoInfo']").text)

driver.find_element_by_xpath("//button[normalize-space()='Place Order']").click()
time.sleep(2)
driver.close()
