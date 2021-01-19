import requests

url = 'http://127.0.0.1:8000/hell/'
headers = {'Authorization': 'Token b05f45d785d1e6faca3ed666aef6332971b040bc'}
r = requests.get(url, headers=headers)
print(r)