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
            print("Артикул найден, первый в списке")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.catalog-card__image'))).click()
        else:
            print("Первым идет другой артикул")
       
    except NoSuchElementException:
        print("Элемент не найден")  

#Get to ERM CZ with the input link
website_erm = input("Ссылка на CZ ERM: ")
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
    print("Краткое описание совпадает")
else:
    print("ОШИБКА! Краткое описание не совпадает")

if big_text_erm == big_text_lev:
    print("Полное описание совпадает")
else:
    print("ОШИБКА! Полное описание не совпадает")
    
# Close the browser
driver.quit()




