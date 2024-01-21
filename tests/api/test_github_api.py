import pytest
# import pdb; 


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    #pdb.set_trace()
    assert r['total_count'] == 54

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    r = github_api.get_emojis()
    assert r['100'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"

@pytest.mark.api
def test_get_emojis_not_found(github_api):
    r = github_api.get_emojis_not_exist()
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_commits_quantity_9(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-06-50', 'my_projects')
    assert len(r) == 9

@pytest.mark.api
def test_commits_commit_0_author_tatiana_belyaeva(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-06-50', 'my_projects')
    assert r[0]['commit']['author']['name'] == 'Tatyana Belyaeva'

@pytest.mark.api
def test_commits_owner_not_exists(github_api):
    r = github_api.list_commits('tat-bor-belyaeva-27-07-50', 'my_projects')
    assert r['message'] == 'Not Found'