import requests

url = "https://yougile.com/api-v2/auth/keys"
data = {
    "login": "yanatimofeeva30@yandex.ru",
    "password": "Liza2011.",
    "companyId": "19d630e0-89b5-4785-9b33-0b48782211e4"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print("Статус:", response.status_code)
print("Ответ:")
print(response.json())
