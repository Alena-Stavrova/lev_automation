#The program gets SKU from the 1st website (link is an input),
#search the same SKU on the 2nd website, go to the item's page
#and compares descriptions on both pages.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# Search SKU, go to the item's page
def find_detail_page(input_sku):
    search_string = "ID výrobku: " + str(input_sku)
    try:
        sku_text = driver.find_element(By.CSS_SELECTOR, '.catalog-card__article').text
        #print(sku_text)
        if sku_text == search_string:
            print("SKU is the first search result")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.catalog-card__image'))).click()
        else:
            print("The first search result has a different SKU")
       
    except NoSuchElementException:
        print("Element not found")  

#Get to ERM CZ with the input link
website_erm = input("Link to CZ ERM: ")
driver = webdriver.Chrome()
driver.get(website_erm)

#Find sku at the ERM CZ page
sku = driver.find_element(By.CSS_SELECTOR, ".specification-table__cell-value span").text
print("Артикул: " + str(sku))

intro_text_erm = driver.find_element(By.CSS_SELECTOR, "div.mt-16").text
#print(intro_text_erm)

big_text_erm = driver.find_element(By.CSS_SELECTOR, "div.wysiwyg.wysiwyg_init").text
#print(big_text_erm)

#Get to LEV CZ homepage
driver.get("https://cz.levenhuk.com/")

#Find search box, input sku
sbox = driver.find_element(By.CSS_SELECTOR, '.header__search span')
sbox.click()
driver.find_element(By.CSS_SELECTOR, '.search__input').send_keys(str(sku) + Keys.ENTER)
find_detail_page(sku)

intro_text_lev = driver.find_element(By.CSS_SELECTOR, "div.mb-48 .pb-md-24").text
#print(intro_text_lev)

big_text_lev = driver.find_element(By.CSS_SELECTOR, "div.wysiwyg.wysiwyg_init").text
#print(big_text_erm)

if intro_text_erm == intro_text_lev:
    print("Short descriptions match")
else:
    print("ERROR! Short descriptions don't match")

if big_text_erm == big_text_lev:
    print("Full descriptions match")
else:
    print("ERROR! Full descriptions don't match")
    
# Close the browser
driver.quit()




