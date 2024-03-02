import pytest

from modules.api.clients.github import GitHub


class User:

    #за допомогою конструктора задаєм поля name та second_name зі значеннями за замовчуванням None
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    # метод об'єкта "створити" (create) задає полям name та second_name значення мого імені та прізвища
    def create(self):
        self.name = "Tatiana"
        self.second_name = "Belyaeva"

    # метод об'єкта "видалити" (remove) задає полям name та second_name значення пустого рядка
    def remove(self):
        self.name = ""
        self.second_name = ""


# описуєм фікстуру user. Ця фікстура створює об'єкт класа User, викликає метод об'єкту create,
# повертає об'єкт після виклику методу об'єкту create в тести,
# після виконання тесту викликає метод об'єкту remove
@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

# описуєм фікстуру github_api. Ця фікстура створює об'єкт класа GitHub
# повертає створений об'єкт в тести
@pytest.fixture
def github_api():
    github_api = GitHub()
    yield github_api