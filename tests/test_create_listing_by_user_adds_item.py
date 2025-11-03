from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL
from locators import LOGIN_BUTTON_HEADER, EXISTING_EMAIL, EXISTING_PASS, \
    SIGN_IN_BUTTON, CREATE_LISTING, LISTING_NAME, LISTING_DESCRIPTION, \
    LISTING_PRICE, DROP_DOWN_CATEGORY, DROP_DOWN_CATEGORY_ITEM, \
    DROP_DOWN_TOWN, DROP_DOWN_TOWN_ITEM, ITEM_CONDITION, PUBLISH_BUTTON, \
    USER_PROFILE_ICON, LISTING_ITEM
from data import EXISTING_EMAIL_STRING, EXISTING_PASSWORD_STRING, \
    LISTING_ITEM_TEXT, LISTING_DESCRIPTION_TEXT, LISTING_PRICE_TEXT
from selenium.common.exceptions import StaleElementReferenceException


def test_create_listing_by_user_adds_item(driver): # 7
    wait = WebDriverWait(driver, 3)

    driver.get(BASE_URL)
    
    # Нажать кнопку «Вход и регистрация».
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_HEADER)).click()

    # Авторизоваться под заранее созданным пользователем.
    wait.until(EC.visibility_of_element_located(EXISTING_EMAIL)).send_keys(EXISTING_EMAIL_STRING)
    wait.until(EC.visibility_of_element_located(EXISTING_PASS)).send_keys(EXISTING_PASSWORD_STRING)
    wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

    try: # to fix "StaleElementReferenceException"
        wait.until(EC.element_to_be_clickable(CREATE_LISTING)).click()
    except StaleElementReferenceException:
        driver.refresh()
        wait.until(EC.element_to_be_clickable(CREATE_LISTING)).click()
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
    wait.until(EC.element_to_be_clickable(USER_PROFILE_ICON)).click()

    # Проверить: в блоке «Мои объявления» отображается созданное объявление.
    element = wait.until(EC.presence_of_element_located(LISTING_ITEM))

    assert element.is_displayed()
    