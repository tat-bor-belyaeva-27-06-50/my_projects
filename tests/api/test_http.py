import pytest
import requests

# test_first_request має мітку http,
# першим кроком тест відправляє http запит методом get на адресу https://api.github.com/zen і
# зберігає відповідь сервера у змінну r;
# другим кроком тест, за допомогою f-рядків виводить на екран атрибут text відповіді від сервера
@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

# test_second_request має мітку http,
# першим кроком тест відправляє http запит методом get на адресу https://api.github.com/users/defunkt 
# i зберігає відповідь сервера у змінну r;
# викликаємо метод json() для перетворення відповіді в об'єкт json;
# тест перевіряє, що атрибут name тіла відповіді від сервера відповідає значенню 'Chris Wanstrath'
# тест перевіряє, що статус-код відповіді від сервера відповідає числу 200
# тест перевіряє, що заголовок Server відповіді від сервера відповідає значенню 'GitHub.com'
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body ['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers ['Server'] == 'GitHub.com'

# test_status_code_request має мітку http,
# першим кроком тест відправляє http запит з методом get на адресу https://api.github.com/users/sergii_butenko 
# i зберігає відповідь сервера у змінну r;
# тест перевіряє, що статус-код відповіді від сервера відповідає числу 404
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404