import pytest

from conftest import User

# test_change_name має мітку check, використовує фікстуру user,
# перевіряє, що поле name об'єкту user відповідає очікуваному
@pytest.mark.check
def test_change_name(user: User):
    assert user.name == 'Tatiana'

# test_change_second_name має мітку check, використовує фікстуру user,
# перевіряє, що поле second_name об'єкту user відповідає очікуваному
@pytest.mark.check
def test_change_second_name(user: User):
    assert user.second_name == 'Belyaeva'
