import requests


class GitHub:
# клас має методи об'єкту get_user і search_repo
    
# в описі методу get_user є обов'язковий параметр username
# в тілі методу формується адреса, на яку потрібно відправити http запит
# Логіка формування адреси-поєднати два рядки: https://api.github.com/users і значення параметра username
# в тілі методу відправляється http запит з методом get на URL-адресу з попереднього кроку
# метод повертає тіло відповіді від сервера у форматі json
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

# в описі методу search_repo є обов'язковий параметр name
# в тілі методу відправляється http запит з методом get на URL-адресу https://api.github.com/search/repositories
# з параметром рядка запиту q, значення якого дорівнює значенню параметра методу name
# метод повертає тіло відповіді від сервера у форматі json  
    def search_repo(self, name):
        r = requests.get(f"https://api.github.com/search/repositories?q={name}")
        body = r.json()

        return body

# в тілі методу get_emojis відправляється http запит з методом get на URL-адресу https://api.github.com/emojis
# метод повертає тіло відповіді у форматі json
    def  get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

# в тілі методу get_emojis_not_exist відправляється http запит з методом get 
# на неіснуючу URL-адресу https://api.github.com/emojis/test
# метод повертає тіло відповіді у форматі json  
    def  get_emojis_not_exist(self):
        r = requests.get("https://api.github.com/emojis/test")
        body = r.json()

        return body

# метод list_commits має обов'язкові параметри owner, repo
# в тілі методу list_commits відправляється http запит з методом get 
# на URL-адресу https://api.github.com/repos/{owner}/{repo}/commits
# метод повертає тіло відповіді у форматі json   
    def list_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()

        return body
