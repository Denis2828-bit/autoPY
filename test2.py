from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def browser():
    """
    Фикстура для инициализации и закрытия браузера.
    """
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


def test_open_s6(browser):
    """
    Тест для проверки открытия страницы "Samsung galaxy s6".
    """
    browser.get('https://demoblaze.com/index.html')
    
    sleep(2) 
    
    galaxy_s6 = browser.find_element(By.LINK_TEXT, value='Samsung galaxy s6')
    galaxy_s6.click()
    
    sleep(2)
    
    title = browser.find_element(By.CSS_SELECTOR, value='h2')
    

    assert title.text == 'Samsung galaxy s6'
    print("Тест пройден!")


def test_two_monitors(browser):
    browser.get('https://demoblaze.com/index.html')
    monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2)
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2