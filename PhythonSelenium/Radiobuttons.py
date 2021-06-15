import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radios = driver.find_elements_by_css_selector("input[type='radio']")
radios[2].click()
assert radios[2].is_selected()