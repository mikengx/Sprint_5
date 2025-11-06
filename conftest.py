import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Завершение работы драйвера после теста
    driver.quit()
