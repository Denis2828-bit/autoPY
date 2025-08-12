from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



@pytest.fixture()
def browser():                                  
    browser = webdriver.Safari()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()



def test_open_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    galaxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]' )
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'
