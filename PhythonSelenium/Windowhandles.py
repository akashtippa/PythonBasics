import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
windowText = driver.find_element_by_tag_name("h3").text
print(windowText)