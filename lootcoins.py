import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_name = os.environ["user"]
password = os.environ["pass"]

driver = webdriver.Remote(
   command_executor='http://hub:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://store.play.net/Account/SignIn?returnURL=%2F")
page_title = driver.title
assert page_title == "Play.net Simucoin Store"
element = driver.find_element_by_id("UserName")
element.send_keys(user_name)
element = driver.find_element_by_id("Password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
wait = WebDriverWait( driver, 5 )

driver.get("https://store.play.net/store/purchase/dr")
try:
    element = driver.find_element_by_class_name("RewardButton")
    element.click()
    print(user_name[:2] + "****** => Looted coins.")
except NoSuchElementException as exception:
    element = driver.find_element_by_class_name("RewardMessage")
    print(user_name[:2] + "****** => " + element.text)
finally:
    driver.close()
