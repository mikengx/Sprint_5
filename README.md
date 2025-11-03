# Проект автоматизации UI тестирования для учебного сервиса «Доска»
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v.

Тесты:
1. Регистрация пользователя - test_create_user_account_creates_account.py
2. Регистрация пользователя c email не по маске - test_user_register_with_incorrect_email_shows_error.py
3. Регистрация уже существующего пользователя - test_user_register_existing_user_shows_error.py
4. Login пользователя - test_user_login_authourizes_user.py
5. Logout пользователя - test_user_logout_works_successfully.py
6. Создание объявления неавторизованным пользователем - test_create_listing_by_guest_fails.py
7. Создание объявления авторизованным пользователем - test_create_listing_by_user_adds_item.py# Sprint_5
