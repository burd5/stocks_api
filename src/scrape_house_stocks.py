from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import read_house_stocks as rhs
soup = BeautifulSoup('html', 'lxml')
driver = webdriver.Chrome()

document_links = []
transaction_reports = []

def open_up_search_table():
    driver.get('https://disclosures-clerk.house.gov/FinancialDisclosure')

    search_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[1]/ul/li[7]/a')
    search_button.click()

    time.sleep(2)

    dropdown = driver.find_element(By.XPATH, '//*[@id="FilingYear"]/option[12]')
    dropdown.click()

    time.sleep(2)

    search_click = driver.find_element(By.XPATH, '//*[@id="search-members"]/form/div[4]/button[1]')
    search_click.click()

    time.sleep(2)

    number_of_pages = int(driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div[3]/div[3]/div/div/div/div[4]/span/a[6]').text)

    find_row_information_for_page_range(1, number_of_pages)

def find_row_information_for_page_range(start = 1, stop = float('inf')):
    for page in range(1, stop):
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//a[text()={page}]")))
        element.click()

        time.sleep(2)

        rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))) 

        find_matching_columns(rows)
   
def find_matching_columns(rows):
    for row in rows:
        cols = row.find_elements(By.TAG_NAME,'td')
        add_matches_to_dictionary(cols)

def add_matches_to_dictionary(cols):
    name = cols[0].text
    office = cols[1].text
    filing_year = cols[2].text
    if cols[3].text == 'PTR Original':
        link_element = cols[0]
        anchor_tag = link_element.find_element(By.TAG_NAME, 'a')
        href = anchor_tag.get_attribute('href')
        
        if href not in document_links:
            document_links.append(href)
            transaction_reports.append(
                {'name': name, 'office': office, 'filing_year': filing_year, 'report_link': href}
            )
    



open_up_search_table()

driver.quit()
print(transaction_reports)
print(document_links)
###








