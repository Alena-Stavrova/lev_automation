#A script that goes through a category (can be 1 or more pages)
#and collects all the skus. Useful for checking the catalog.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

website_erm = input("Ссылка на категорию CZ ERM: ")
driver = webdriver.Chrome()

def process_category_page(url, page_number):
    load_page(url, page_number) 
    page_skus = parse_skus()
    next_page_present = detect_next_page_button()
    return(page_skus, next_page_present) 

def load_page(url, page_n): #should contain all the manipulations with the url
    if page_n == 1:
        target_url = url
    else:
        target_url = url + "/?PAGEN_1=" + str(page_n)
    driver.get(target_url)
    #time.sleep(3)

def parse_skus():
    skus = []
    while True:
        time.sleep(1)
        elems = driver.find_elements(By.CSS_SELECTOR, ".product-card__article")
        emptyElem = None
        for el in elems:
            if el.text == '':
                emptyElem = el
                #print(emptyElem.text)
                break
            new_sku = el.text[4:]
            if new_sku not in skus:
                skus.append(new_sku)
        if emptyElem is None:
            break
        driver.execute_script("arguments[0].scrollIntoView(true)", emptyElem)
        print("retrying")
    return(skus)
    #print("Найдено " + str(len(skus)) + " товаров")

def detect_next_page_button():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, "div.pagination__list a.btn")
        current_page = driver.find_element(By.CSS_SELECTOR, "div.pagination__list a.btn.btn-secondary.active").text
        #print(len(elems), current_page)
        if int(current_page) < len(elems):
            return(True)
        else:
            return(False)            
    except NoSuchElementException:
        return(False)

def main(url):
    all_skus = []
    page = 1
    while True:
        page_skus, has_next = process_category_page(url, page)
        #print('page', page, 'contains skus:', page_skus)
        all_skus += page_skus #check if this syntax works
        if not has_next:
            break
        page += 1
    print(all_skus)
    print("Всего найдено " + str(len(all_skus)) + " SKUs")

main(website_erm)
