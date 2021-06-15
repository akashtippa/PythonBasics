from ctypes.macholib.dyld import dyld_executable_path_search

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser

# driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Drivers\\BrowserDriver\\Firefoxdriver\\geckodriver.exe")
driver = webdriver.Edge("C:\\Drivers\\BrowserDriver\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window()
driver.get("http://rahulshettyacademy.com/");

print(driver.title)

print(driver.current_url)

driver.get("https://rahulshettyacademy.com/#/practice-project")

driver.back()

driver.refresh()
driver.close()
