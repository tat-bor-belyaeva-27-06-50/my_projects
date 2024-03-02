import pytest

# test_user_exists має мітку api, відноситься до фікстури github_api,
# в тілі тесту використовується метод get_user фікстури github_api,
# використовується ім'я користувача для пошуку defunkt,
# перевіряється, що тіло відповіді від сервера має атрибут login, значення якого має дорівнювати defunkt
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

# test_user_not_exists має мітку api, відноситься до фікстури github_api,
# в тілі тесту використовується метод get_user фікстури github_api,
# використовується ім'я користувача для пошуку butenkosergii,
# перевіряється, що тіло відповіді від сервера має атрибут message, значення якого має дорівнювати Not Found
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

# test_repo_can_be_found має мітку api, відноситься до фікстури github_api,
# в тілі тесту використовується метод search_repo фікстури github_api,
# використовується ім'я репозиторія для пошуку become-qa-auto,
# перевіряється, що тіло відповіді від сервера має атрибут total_count, значення якого має дорівнювати
# очікуваному на момент створення тесту значенню 54
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54

# test_repo_cannot_be_found має мітку api, відноситься до фікстури github_api,
# в тілі тесту використовується метод search_repo фікстури github_api,
# використовується ім'я репозиторія для пошуку sergiibutenko_repo_non_exist, що не існує на момент створення тесту
# перевіряється, що тіло відповіді від сервера має атрибут total_count, значення якого має дорівнювати 0
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# test_repo_with_single_char_be_found має мітку api, відноситься до фікстури github_api,
# в тілі тесту використовується метод search_repo фікстури github_api,
# використовується ім'я репозиторія для пошуку 's', що складається з одного символу
# перевіряється, що тіло відповіді від сервера має атрибут total_count, значення якого має не дорівнювати 0
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# test_get_emojis має мітку api, відноситься до фікстури github_api,
# в тілі тесту викликається метод get_emojis фікстури github_api
# з параметрами unicode, 1f4af.png
# перевіряється, що відповід має атрібут "100", 
# значення якого дорівнює "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"
@pytest.mark.api
def test_get_emojis(github_api):
    r = github_api.get_emojis()
    assert r['100'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"

# test_get_emojis_not_found має мітку api, відноситься до фікстури github_api,
# в тілі тесту викликається неіснуючий метод test у фікстурі github_api
# перевіряється, що сервер повертая помилку 404, Not Found
@pytest.mark.api
def test_get_emojis_not_found(github_api):
    r = github_api.get_emojis_not_exist()
    assert r['message'] == 'Not Found'

# test_commits_quantity_9 має мітку api, відноситься до фікстури github_api,
# в тілі тесту викликається метод list_commits у фікстурі github_api
# перевіряться, що кількість комітів у репозиторії my_projects,
# зроблених користувачем tat-bor-belyaeva-27-06-50, дорівнює 9 
@pytest.mark.api
def test_commits_quantity_9(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-06-50', 'my_projects')
    assert len(r) == 9

# test_commits_commit_0_author_tatiana_belyaeva має мітку api, відноситься до фікстури github_api,
# в тілі тесту викликається метод list_commits у фікстурі github_api
# перевіряться, що ім'я автора комітів у репозиторії my_projects,
# дорівнює Tatyana Belyaeva
@pytest.mark.api
def test_commits_commit_0_author_tatiana_belyaeva(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-06-50', 'my_projects')
    assert r[0]['commit']['author']['name'] == 'Tatyana Belyaeva'

# test_commits_owner_not_exists має мітку api, відноситься до фікстури github_api,
# в тілі тесту викликається метод list_commits у фікстурі github_api для
# неіснуючого користувача
# перевіряється, що метод повертає 404 - Not Found
@pytest.mark.api
def test_commits_owner_not_exists(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-07-50', 'my_projects')
    assert r['message'] == 'Not Found'