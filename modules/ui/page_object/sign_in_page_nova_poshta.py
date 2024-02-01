from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPageNovaPoshta(BasePage):
    URL = 'https://new.novaposhta.ua/auth/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageNovaPoshta.URL)

    def check_error_message(self):
        login_elem = self.driver.find_element(By.NAME, "email")

        error_attribute = login_elem.get_attribute("aria-invalid")

        print("aria-invalid")
        print(error_attribute)
        print("aria-invalid")
        assert error_attribute != None

        password_elem = self.driver.find_element(By.NAME, "password")
        error_attribute = password_elem.get_attribute("aria-invalid")

        print(error_attribute)
        assert error_attribute != None

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        #login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem = self.driver.find_element(By.NAME, "email")

        # Вводимо неправильне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.NAME, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку увійти
        btn_elem = self.driver.find_element(By.CLASS_NAME, "np-red-btn")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    

