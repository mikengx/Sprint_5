from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_HEADER, NO_ACCOUNT_BUTTON, EMAIL_INPUT, \
    PASSWORD_INPUT_1, PASSWORD_INPUT_2, CREATE_ACCOUNT_BUTTON, USER_AVATAR, USER_TEXT
from urls import BASE_URL, REG_URL
from data import EXAMPLE_PASSWORD, USER_AVATAR_TEXT
from utils import generate_test_email


def test_create_user_account_creates_account(driver): # 1
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
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

    assert driver.current_url == REG_URL and avatar_svg.is_displayed() and \
        user_text == USER_AVATAR_TEXT
