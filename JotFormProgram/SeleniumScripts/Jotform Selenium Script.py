import em as em
from selenium import webdriver

driver = webdriver.Chrome("C:\Selenium\Chrome\chromedriver.exe")
driver.get("https://www.jotform.com/200154713399152")
driver.maximize_window()

# enter a valid quantity
driver.find_element_by_id('input_44').send_keys('Store')
driver.find_element_by_id('input_32').send_keys('ProdToLoad')
