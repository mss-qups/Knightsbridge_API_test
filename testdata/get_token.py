import requests
import json

url = "http://47.251.2.96:3000/api/users/signin"
# url = "https://api-dev.knightsbridge.live/api/users/signin"
payload = json.dumps({"email": "user@mail.com", "password": "ndsfG@jJdf4325sg"})
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)
body = response.json()
token = body['token']
