from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Copy and paste the link to an item on ERM CZ
website_erm = input("Link to CZ ERM: ")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

#Navigate to Ermenrich CZ
#website_erm = "https://cz.ermenrich.com/catalogue/laserove-a-opticke-vodovahy/laserove-vodovahy/laserovy-nivelacni-pristroj-ermenrich-lv50-pro/?oid=679"
#website_erm = "https://cz.ermenrich.com/catalogue/digitalni-vodovahy-a-uhlomery/digitalni-vodovahy/digitalni-vodovaha-ermenrich-verk-lq20/?oid=717"
driver.get(website_erm)

#Find sku by custom css selector 
sku = driver.find_element(By.CSS_SELECTOR, ".specification-table__cell-value span").text
print("Target SKU is: " + str(sku))

# Navigate to the website
driver.get("https://cz.levenhuk.com/")

def check_exists_by_sku(example_sku):
    search_string = "ID výrobku: " + str(example_sku)
    try:
        sku_text = driver.find_element(By.CSS_SELECTOR, '.catalog-card__article').text
        #print(sku_text)
        if sku_text == search_string:
            print("First result matches the SKU")
        else:
            print("First result DOES NOT match the SKU")
       
    except NoSuchElementException:
        print('Element not found')

#Find search box, input sku
sbox = driver.find_element(By.CSS_SELECTOR, '.header__search span')
sbox.click()
driver.find_element(By.CSS_SELECTOR, '.search__input').send_keys(str(sku) + Keys.ENTER)
check_exists_by_sku(sku)

# Close the browser
driver.quit()


