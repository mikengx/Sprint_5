from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import LOGIN_BUTTON_HEADER, EXISTING_EMAIL, EXISTING_PASS, \
    SIGN_IN_BUTTON, USER_AVATAR, USER_TEXT, SIGN_IN_HEADER, SIGN_OUT_BUTTON
from data import EXISTING_EMAIL_STRING, EXISTING_PASSWORD_STRING


def test_user_logout_works_successfully(driver): # 5
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
    # Нажать кнопку «Вход и регистрация».
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
    
    # Авторизоваться под заранее созданным пользователем.
    wait.until(EC.visibility_of_element_located(EXISTING_EMAIL)).send_keys(EXISTING_EMAIL_STRING)
    wait.until(EC.visibility_of_element_located(EXISTING_PASS)).send_keys(EXISTING_PASSWORD_STRING)
    wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

    # Нажать кнопку «Выйти».
    wait.until(EC.element_to_be_clickable(SIGN_OUT_BUTTON)).click()

    # Проверить: аватар пользователя и имя User больше не отображается 
    # в правом верхнем углу около кнопки «Разместить объявление»,
    # там теперь отображается кнопка «Вход и регистрация».
    sign_in_text = wait.until(EC.visibility_of_element_located(SIGN_IN_HEADER)).text
    avatar_svg = driver.find_elements(*USER_AVATAR)
    user_text = driver.find_elements(*USER_TEXT)

    assert len(avatar_svg) == 0 and len(user_text) == 0 and sign_in_text == 'Вход и регистрация'
