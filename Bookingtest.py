import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestMainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com/")

    def test_booking(self):
        driver = self.driver
        driver.find_element(By.NAME, "ss").click()
        driver.find_element(By.NAME, "ss").send_keys("Berlin")
        driver.find_element(By.NAME, "ss").send_keys(Keys.RETURN)
        self.assertNotEqual(self.driver.current_url, "https://www.booking.com/")
        name = 'images/' + 'book' + '.png'
        print(name)
        driver.save_screenshot(name)

    def tearDown(self):
        self.driver.quit()
        ##