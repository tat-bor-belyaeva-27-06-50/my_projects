import pytest

# test_remove_name має мітку change, відноситься до фікстури user,
# першим кроком тест змінює поле name об'єкта user на пустий рядок,
# другим кроком тест перевіряє, що зміни відбулися і вони правильні
@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

# test_name має мітку check, відноситься до фікстури user,
# перевіряє, що поле name об'єкту user відповідає очікуваному
@pytest.mark.check
def test_name(user):
    assert user.name == "Tatiana"

# test_second_name має мітку check, відноситься до фікстури user,
# перевіряє, що поле second_name об'єкту user відповідає очікуваному
@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Belyaeva"