from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class SignInPageRozetka(BasePage):
    URL = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageRozetka.URL)

    def check_error_message(self):
        login_elem = self.driver.find_element(By.ID, "phone")

        # отримуємо батьківський елемент у login_elem, тому що атрибут class зі значенням 
        # "validation_type_error" з'являється тільки у батьківського елемента
        parent_login = login_elem.find_element(By.XPATH, '..')

        # отримуємо атрибут class у батьківського елемента  login_elem
        classes = parent_login.get_attribute("class")

        # перевіряємо наявність тексту validation_type_error у змінній classes 
        assert "validation_type_error" in classes       
       
    def try_login(self, username):
        # Знаходимо кнопку відкриття діалогового вікна для входу на сайт
        login_btn_elem = self.driver.find_element(By.TAG_NAME, "rz-user")

        # у login_btn_elem серед дітей знаходимо елемент з типом type='button
        login_btn = login_btn_elem.find_element(By.CSS_SELECTOR, "[type='button']")
        
        login_btn.click()

        time.sleep(5)

        print('dialog was opened')

        # Знаходимо поле, в яке будемо вводити неправильний номер телефону
        login_elem = self.driver.find_element(By.ID, "phone")

        # Вводимо неправильний номер користувача
        login_elem.send_keys(username)

        # Знаходимо кнопку продовжити
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    

