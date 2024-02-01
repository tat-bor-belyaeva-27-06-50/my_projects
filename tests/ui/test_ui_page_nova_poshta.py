from modules.ui.page_object.sign_in_page_nova_poshta import SignInPageNovaPoshta
import pytest
#import time

@pytest.mark.nova_poshta
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPageNovaPoshta()

    # відкриваємо сторінку https://new.novaposhta.ua/auth/login 
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему Nova Poshta
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #time.sleep(5)

    # перевіряємо, що на сторінці є повідомлення про помилку
    sign_in_page.check_error_message()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Бізнес-кабінет - Нова пошта")

    # Закриваємо браузер
    sign_in_page.close()
