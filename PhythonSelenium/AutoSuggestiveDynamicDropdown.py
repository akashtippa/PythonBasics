import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
CountryList = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(CountryList))
for country in CountryList:
    if country.text == "India":
        country.click()
        break

time.sleep(2)
# driver.find_element_by_id("autosuggest").text
assert driver.find_element_by_id("autosuggest").get_attribute('value') =="India"
driver.close()
