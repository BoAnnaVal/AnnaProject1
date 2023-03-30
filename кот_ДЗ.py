from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

try:
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys("кот")
    elem.send_keys(Keys.RETURN)

    print("Поиск выполнен успешно")
except:
    print("Ошибка: страница со словом 'кот' не найдена")

    driver.close()