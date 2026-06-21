# test.py

import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"sqlcoder",
        "prompt":"Generate SQL to get all users"
    }
)

print(response.text)