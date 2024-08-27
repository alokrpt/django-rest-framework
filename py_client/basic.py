import requests

endpoint = "https://www.github.com"
endpoint = "https://reqres.in/api/users?page=2"
endpoint = "http://localhost:8000/api"

res = requests.get(endpoint)
print(res.json())
print(res.status_code)
