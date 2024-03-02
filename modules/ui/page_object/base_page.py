from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    DRIVER_NAME = "chromedriver"

# в конструкторі класу ініціалізується об'єкт для комунікації з вебдрайвером
# клас має метод об'єкта close, задача якого закрити відкритий браузер

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()
