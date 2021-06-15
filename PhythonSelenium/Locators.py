

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("TestMe")
driver.find_element_by_name("email").send_keys("testme@yopmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Test@123")
driver.find_element_by_id("exampleCheck1").click()

# select class provide the methods to handle the options in dropdown

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@value='Submit']").click()
alertMessage = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(alertMessage)
assert "success" in alertMessage

driver.close()