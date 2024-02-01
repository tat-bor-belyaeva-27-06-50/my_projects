from modules.ui.page_object.sign_in_page_rozetka import SignInPageRozetka
import pytest
import time

@pytest.mark.rozetka
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPageRozetka()

    # відкриваємо сторінку https://rozetka.com.ua/ua/ 
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему Rozetka
    sign_in_page.try_login("9999999999")

    time.sleep(5)

    # перевіряємо, що на сторінці є повідомлення про помилку
    sign_in_page.check_error_message()
   
    # Закриваємо браузер
    sign_in_page.close()
