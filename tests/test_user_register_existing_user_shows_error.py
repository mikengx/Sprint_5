from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_HEADER, NO_ACCOUNT_BUTTON, EMAIL_INPUT, \
    PASSWORD_INPUT_1, PASSWORD_INPUT_2, CREATE_ACCOUNT_BUTTON, EMAIL_BORDER, \
    PWD_1_BORDER, PWD_2_BORDER, ERROR_TEXT_LOGIN
from urls import BASE_URL
from data import EXISTING_EMAIL_STRING, EXISTING_PASSWORD_STRING, \
    ERROR_BORDER_COLOR, ERROR_TEXT_STRING


def test_user_register_existing_user_shows_error(driver): # 3
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
    # Нажать кнопку «Вход и регистрация».
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
    
    # Нажать кнопку «Нет аккаунта».
    wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EXISTING_EMAIL_STRING)
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(EXISTING_PASSWORD_STRING)
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_2)).send_keys(EXISTING_PASSWORD_STRING)
    wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, 
    # под полем Email отображается сообщение «Ошибка».
    error_text = wait.until(EC.visibility_of_element_located(ERROR_TEXT_LOGIN)).text
    email_border_prop = driver.find_element(*EMAIL_BORDER).value_of_css_property('border')
    pwd_1_border_prop = driver.find_element(*PWD_1_BORDER).value_of_css_property('border')
    pwd_2_border_prop = driver.find_element(*PWD_2_BORDER).value_of_css_property('border')

    assert ERROR_BORDER_COLOR in email_border_prop and \
        ERROR_BORDER_COLOR in pwd_1_border_prop and \
        ERROR_BORDER_COLOR in pwd_2_border_prop and \
        error_text == ERROR_TEXT_STRING
