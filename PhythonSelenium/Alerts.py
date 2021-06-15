import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input[name='enter-name']").send_keys("Test Alert")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
text = alert.text

print(alert.text)

assert "Test" in text
alert.accept()

time.sleep(2)

driver.find_element_by_css_selector("input[name='enter-name']").send_keys("dismiss")
driver.find_element_by_id("confirmbtn").click()

alert = driver.switch_to.alert
text1 = alert.text

print(alert.text)

assert "dismiss" in text1
alert.dismiss()

