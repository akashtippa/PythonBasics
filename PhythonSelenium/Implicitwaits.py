import time

from selenium import webdriver
# Implicit waits
# Explicit waits
# pause the test for secconds using time class
list1 = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Drivers\\BrowserDriver\\chromedriver90\\chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(7)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(4)
# valaidate products counts
ProdCount = len(driver.find_elements_by_css_selector("div[class='product']"))
print(ProdCount)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    # backtraverse button to parent then h4
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list1)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_css_selector("div[class='cart-preview active'] button[type='button']").click()
time.sleep(2)
veggies = driver.find_elements_by_css_selector("p[class='product-name']")
for veg in veggies:
    list2.append(veg.text)


print(list2)

assert list1 == list2
originalAmount = driver.find_element_by_css_selector("span.discountAmt").text
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
print(driver.find_element_by_css_selector("span[class='promoInfo']").text)
DiscountAmount = driver.find_element_by_css_selector("span.discountAmt").text
assert float(DiscountAmount) < int(originalAmount)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
TotalAmount = driver.find_element_by_xpath("//span[@class='totAmt']").text
sum =0
for amount in amounts:
    sum = sum + int(amount.text)

assert originalAmount == TotalAmount
driver.find_element_by_xpath("//button[normalize-space()='Place Order']").click()

driver.close()