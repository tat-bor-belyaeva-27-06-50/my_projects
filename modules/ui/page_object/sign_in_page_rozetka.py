from typing import KeysView
from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SignInPageRozetka(BasePage):
    URL = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageRozetka.URL)

    def check_error_message(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "validation-message")))
            parent_login = self.driver.find_element(By.CLASS_NAME, 'validation-message')
        except:
            parent_login = self.driver.find_element(By.CLASS_NAME, 'error-message')
            
        assert parent_login != None   
       
    def try_login(self, username):
        # Знаходимо кнопку відкриття діалогового вікна для входу на сайт
        login_btn_elem = self.driver.find_element(By.TAG_NAME, "rz-user")

        # у login_btn_elem серед дітей знаходимо елемент з типом type='button
        login_btn = login_btn_elem.find_element(By.CSS_SELECTOR, "[type='button']")
        
        login_btn.click()

        # Знаходимо поле, в яке будемо вводити неправильний номер телефону
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "phone")))
            login_elem = self.driver.find_element(By.ID, "phone")
        except:
            login_elem = self.driver.find_element(By.ID, "auth_email")

        # Вводимо неправильний номер користувача
        login_elem.send_keys(username)

        # Натискаємо кнопку TAB на клавіатурі для переходу на інше поле вводу
        login_elem.send_keys(Keys.TAB)

    

