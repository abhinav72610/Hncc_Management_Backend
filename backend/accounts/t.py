import requests
import json
session = requests.session()
data = {
    "username": "Abhi",
    "password": "Abhinav_It_003"
}
r = session.post("http://127.0.0.1:8000/api/login/", json=data)
re = r.json()
