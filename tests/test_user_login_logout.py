from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import baseUrl
from locators import LOGIN_BUTTON_HEADER, EMAIL_INPUT, PASSWORD_INPUT_1, \
    CREATE_ACCOUNT_BUTTON, USER_AVATAR, USER_TEXT, SIGN_OUT_BUTTON, LOGIN_BUTTON_HEADER
from data import EMAIL_INPUT_STRING, PASSWORD_INPUT_1WORD_STRING, USER_AVATAR_TEXT


class TestUserLoginLogout:

    def test_user_login_authourizes_user(self, driver): # 4
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()

        # Авторизоваться под заранее созданным пользователем.
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EMAIL_INPUT_STRING)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(PASSWORD_INPUT_1WORD_STRING)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        # Проверить: произошёл переход на главную страницу, 
        # в правом верхнем углу около кнопки «Разместить объявление» 
        # отображается аватар пользователя и имя User.
        avatar_svg = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        user_text = wait.until(EC.visibility_of_element_located(USER_TEXT)).text

        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/login'and \
            avatar_svg.is_displayed() and \
            user_text == USER_AVATAR_TEXT


    def test_user_logout_works_successfully(self, driver): # 5
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()
        
        # Авторизоваться под заранее созданным пользователем.
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EMAIL_INPUT_STRING)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(PASSWORD_INPUT_1WORD_STRING)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        # Нажать кнопку «Выйти».
        wait.until(EC.element_to_be_clickable(SIGN_OUT_BUTTON)).click()

        # Проверить: аватар пользователя и имя User больше не отображается 
        # в правом верхнем углу около кнопки «Разместить объявление»,
        # там теперь отображается кнопка «Вход и регистрация».
        sign_in_text = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON_HEADER)).text
        avatar_svg = driver.find_elements(*USER_AVATAR)
        user_text = driver.find_elements(*USER_TEXT)

        assert len(avatar_svg) == 0 and len(user_text) == 0 and sign_in_text == 'Вход и регистрация'
