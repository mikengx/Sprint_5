from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import LOGIN_BUTTON_HEADER, EXISTING_EMAIL, EXISTING_PASS, \
    SIGN_IN_BUTTON, USER_AVATAR, USER_TEXT
from data import EXISTING_EMAIL_STRING, EXISTING_PASSWORD_STRING, USER_AVATAR_TEXT


def test_user_login_authourizes_user(driver): # 4
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
    # Нажать кнопку «Вход и регистрация».
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()

    # Авторизоваться под заранее созданным пользователем.
    wait.until(EC.visibility_of_element_located(EXISTING_EMAIL)).send_keys(EXISTING_EMAIL_STRING)
    wait.until(EC.visibility_of_element_located(EXISTING_PASS)).send_keys(EXISTING_PASSWORD_STRING)
    wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

    # Проверить: произошёл переход на главную страницу, 
    # в правом верхнем углу около кнопки «Разместить объявление» 
    # отображается аватар пользователя и имя User.
    avatar_svg = wait.until(EC.visibility_of_element_located(USER_AVATAR))
    user_text = wait.until(EC.visibility_of_element_located(USER_TEXT)).text

    assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/login'and \
        avatar_svg.is_displayed() and \
        user_text == USER_AVATAR_TEXT
