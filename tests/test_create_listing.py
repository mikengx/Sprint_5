from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import baseUrl
from locators import PLACE_LISTING_BUTTON, AUTHORIZE_TEXT, LOGIN_BUTTON_HEADER, \
    EMAIL_INPUT, PASSWORD_INPUT_1, CREATE_ACCOUNT_BUTTON, PLACE_LISTING_BUTTON, \
    LISTING_NAME, LISTING_DESCRIPTION, LISTING_PRICE, DROP_DOWN_CATEGORY, \
    DROP_DOWN_CATEGORY_ITEM, DROP_DOWN_TOWN, DROP_DOWN_TOWN_ITEM, ITEM_CONDITION, \
    PUBLISH_BUTTON, USER_AVATAR, LISTING_ITEM
from data import AUTH_PROMPT_TEXT, EMAIL_INPUT_STRING, PASSWORD_INPUT_1WORD_STRING, \
    LISTING_ITEM_TEXT, LISTING_DESCRIPTION_TEXT, LISTING_PRICE_TEXT
from selenium.common.exceptions import StaleElementReferenceException


class TestCreateListing:

    def test_create_listing_by_guest_fails(self, driver): # 6
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Разместить объявление».
        wait.until(EC.element_to_be_clickable(PLACE_LISTING_BUTTON)).click()
        
        # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        authorize_text = wait.until(EC.visibility_of_element_located(AUTHORIZE_TEXT)).text

        assert authorize_text == AUTH_PROMPT_TEXT


    def test_create_listing_by_user_adds_item(self, driver): # 7
        wait = WebDriverWait(driver, 3)

        driver.get(baseUrl)
        
        # Нажать кнопку «Вход и регистрация».
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()

        # Авторизоваться под заранее созданным пользователем.
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(EMAIL_INPUT_STRING)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_1)).send_keys(PASSWORD_INPUT_1WORD_STRING)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        try: # to fix "StaleElementReferenceException"
            wait.until(EC.element_to_be_clickable(PLACE_LISTING_BUTTON)).click()
        except StaleElementReferenceException:
            driver.refresh()
            wait.until(EC.element_to_be_clickable(PLACE_LISTING_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LISTING_NAME)).send_keys(LISTING_ITEM_TEXT)
        wait.until(EC.visibility_of_element_located(LISTING_DESCRIPTION)).send_keys(LISTING_DESCRIPTION_TEXT)
        wait.until(EC.visibility_of_element_located(LISTING_PRICE)).send_keys(LISTING_PRICE_TEXT)

        # Выбрать из Dropdown «Категорию»
        wait.until(EC.element_to_be_clickable((DROP_DOWN_CATEGORY))).click()
        wait.until(EC.element_to_be_clickable((DROP_DOWN_CATEGORY_ITEM))).click() # "Технологии"

        # и «Город»
        wait.until(EC.element_to_be_clickable(DROP_DOWN_TOWN)).click()
        wait.until(EC.element_to_be_clickable(DROP_DOWN_TOWN_ITEM)).click() # "Казань"

        # Выбрать RabioButton «Состояние товара».
        wait.until(EC.element_to_be_clickable(ITEM_CONDITION)).click() # Б/У

        # Нажать кнопку «Опубликовать».
        driver.find_element(*PUBLISH_BUTTON).click()
        
        # Перейти в профиль пользователя.
        driver.refresh() # to fix "StaleElementReferenceException"
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()

        # Проверить: в блоке «Мои объявления» отображается созданное объявление.
        element = wait.until(EC.presence_of_element_located(LISTING_ITEM))

        assert element.is_displayed()
        