from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org/wiki/Кошка ")

try:
    head_page = driver.find_element(By.XPATH, '/html/body/div[3]/h1/span')
    print("выполнен")
    print(head_page.text)
    if head_page.text == "Кошка":
        print("Текст соответствует ожиданию")
    else:
        print("Текст не соответствует ожиданию")

except:
    print("не выполнен")

search_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/form/div/input[1]")
search_field.clear()
search_field.send_keys(driver.find_element(By.XPATH,"/html/body/div[3]/h1/span").get_attribute("textContent"))

search_field = 'images1/'+"кошки"+'.png'
print(search_field)
driver.save_screenshot(search_field)

time.sleep(5)
driver.close()
