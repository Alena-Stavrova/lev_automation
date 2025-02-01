from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

#Copy and paste the link to an item on ERM CZ
website_erm = input("Ссылка на CZ ERM: ")
driver = webdriver.Chrome()

#The target link looks like this:
#https://cz.ermenrich.com/catalogue/pasmova-meridla/laserove-merice/?PAGEN_1=2

def next_page(my_link):
    driver.get(my_link)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #Check if there are any other pages
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, "div.pagination__list a.btn")
        current_page = driver.find_element(By.CSS_SELECTOR, "div.pagination__list a.btn.btn-secondary.active").text
        #next_page = int(current_page) + 1
        #print(current_page, next_page)
        next_page_link = my_link + "/?PAGEN_1=" + str(int(current_page) + 1)
        #print(next_page_link)
        driver.get(next_page_link)
        time.sleep(5)
        
    except NoSuchElementException:
        print("One page only") 

next_page(website_erm)

# Close the browser
driver.quit()
