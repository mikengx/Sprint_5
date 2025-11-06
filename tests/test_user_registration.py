from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_HEADER, NO_ACCOUNT_BUTTON, EMAIL_INPUT, \
    PASSWORD_INPUT_1, PASSWORD_INPUT_2, CREATE_ACCOUNT_BUTTON, USER_AVATAR, \
    USER_TEXT, EMAIL_BORDER, PWD_1_BORDER, PWD_2_BORDER, ERROR_TEXT_LOGIN
from urls import baseUrl, regUrl
from data import EXAMPLE_PASSWORD, USER_AVATAR_TEXT, ERROR_BORDER_COLOR, \
    ERROR_TEXT_STRING, EMAIL_INPUT_STRING, PASSWORD_INPUT_1WORD_STRING
from utils import generate_test_email, generate_incorrect_email


class TestUserRegistration:

    def test_create_user_account_creates_account(self, driver): # 1
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
        
        # Нажать кнопку «Нет аккаунта».
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        fake_email = generate_test_email()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(fake_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(EXAMPLE_PASSWORD)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_2)).send_keys(EXAMPLE_PASSWORD)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        # Проверить: произошёл переход на главную страницу, 
        # в правом верхнем углу около кнопки «Разместить объявление» 
        # отображается аватар пользователя и имя User.
        avatar_svg = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        user_text = wait.until(EC.visibility_of_element_located(USER_TEXT)).text

        assert driver.current_url == regUrl and avatar_svg.is_displayed() and \
            user_text == USER_AVATAR_TEXT


    def test_user_register_with_incorrect_email_shows_error(self, driver): # 2
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
        
        # Нажать кнопку «Нет аккаунта».
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        incorrect_email = generate_incorrect_email()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(incorrect_email)
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

    def test_user_register_existing_user_shows_error(self, driver): # 3
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
        
        # Нажать кнопку «Нет аккаунта».
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EMAIL_INPUT_STRING)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(PASSWORD_INPUT_1WORD_STRING)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_2)).send_keys(PASSWORD_INPUT_1WORD_STRING)
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
