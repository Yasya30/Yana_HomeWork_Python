import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_auth():
    token = os.getenv("YOUILE_TOKEN")
    url = "https://api.yougile.com/api-v2/projects"
    
    # Вариант 1: Bearer
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"Bearer: {response.status_code}")
    
    # Вариант 2: Только токен
    headers2 = {"Authorization": token}
    response2 = requests.get(url, headers=headers2)
    print(f"Only token: {response2.status_code}")
    
    # Вариант 3: X-API-Key
    headers3 = {"X-API-Key": token}
    response3 = requests.get(url, headers=headers3)
    print(f"X-API-Key: {response3.status_code}")
    
    assert response.status_code == 200, "Не удалось авторизоваться"