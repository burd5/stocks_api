from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import read_house_stocks as rhs

driver = webdriver.Chrome()
driver.get('https://disclosures-clerk.house.gov/FinancialDisclosure')

search_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[1]/ul/li[7]/a')
search_button.click()

time.sleep(3)

dropdown = driver.find_element(By.XPATH, '//*[@id="FilingYear"]/option[12]')

dropdown.click()

time.sleep(3)

search_click = driver.find_element(By.XPATH, '//*[@id="search-members"]/form/div[4]/button[1]')

search_click.click()
time.sleep(10)

number_of_pages = int(driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div[3]/div[3]/div/div/div/div[4]/span/a[6]').text)

###

print(number_of_pages)


driver.quit()



