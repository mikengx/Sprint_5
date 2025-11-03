from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL
from locators import PLACE_LISTING_BUTTON, AUTHORIZE_TEXT
from data import AUTH_PROMPT_TEXT


def test_create_listing_by_guest_fails(driver): # 6
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
    # Нажать кнопку «Разместить объявление».
    wait.until(EC.element_to_be_clickable(PLACE_LISTING_BUTTON)).click()
    
    # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    authorize_text = wait.until(EC.visibility_of_element_located(AUTHORIZE_TEXT)).text

    assert authorize_text == AUTH_PROMPT_TEXT
