from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=800,600")
chrome_options.add_argument('disable-gpu')
driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe",
                          options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)  # get title
