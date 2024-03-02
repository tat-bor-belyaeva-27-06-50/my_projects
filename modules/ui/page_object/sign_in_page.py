from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By

# клас SignInPage наслідуваний від класу BasePage
class SignInPage(BasePage):
    URL = 'https://github.com/login'

# в конструкторі класу викликається конструктор батьківського класу
# в класі реалізований метод об'єкту try_login, який приймає параметри username і password. Задача цього
# методу ввести в поле email ім'я користувача, в поле password пароль і натиснути кнопку sign in
    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильне ім'я користувача або поштову адрІесу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    # метод об'єкту check_title перевіряє, чи відповідає заголовок сторінки очікуваному
    def check_title(self, expected_title):
        return self.driver.title == expected_title

    

