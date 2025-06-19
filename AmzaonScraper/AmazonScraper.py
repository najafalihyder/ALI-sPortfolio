from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)...")# adding an user agent 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # hiding flags of automation
    options.add_experimental_option("useAutomationExtension", False) # removing the massage flag of automation and pretend to be manual to simulate a human

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})                                        # these lines means that when we start browser (driver) it acts as a automation
                                         # becuase selenium automaitacly sets the flasg to show atumation to True sowe setted them again on False pass
                                                                                    
    return driver



def search_products(driver, query):
    url = "https://www.amazon.com"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def extract_products(driver):

    products = []
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    product_elements = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
    for product in product_elements:
        
        try:
            title = product.find_element(By.CSS_SELECTOR, "h2 span").text
        except:
            title = "no title"

        try:
            whole_price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            friction_price = product.find_element(By.CSS_SELECTOR, "a-price-fraction").text
            price = f"{whole_price}.{friction_price}"
            price = float(price.replace("", "$").replace(",", " "))
        except:
            price = None

        try:
            rating  = product.find_element(By.CSS_SELECTOR, "i[aria-label='true'] span.a-icon-alt").text
        except:
            rating = "no rating"

        try:
            image_link = product.find_element(By.CSS_SELECTOR, "img").get_attribute('src')
        except:
            image_link = "No image"

        try:
            url = product.find_element(By.CSS_SELECTOR, "div[data-cy='title-recipe'] a.a-link-normal").get_attribute('href')
        except:
            url = "not url"

        products.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Image": image_link,
            "Url": url
        })

    return products


def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-next")
        next_button.execute_script("arguments[0].click();", next_button)
        return True
    except:
        return False



def main():
    driver = setup_driver()
    query = "coding laptops"
    search_products(driver, query)
    all_products = []

    for page in range(1, 4):  # Adjust the range for more pages
        print(f"Scraping page {page}...")
        products = extract_products(driver)
        all_products.extend(products)
        if not go_to_next_page(driver):
            break
        time.sleep(2)  # Wait for the next page to load

    driver.quit()

    with open("AmazonProducts.json", "w", encoding="utf-8") as file:
        json.dump(all_products, file, indent=4, ensure_ascii=False)

    print("File saved successfully.")  

if __name__ == "__main__":
    main()






