import json
import requests

# url for the autogen server /runs
url = "http://127.0.0.1:8001/runs"

# request headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# payload to send to autogen server for /runs
payload = json.dumps({
    "input": [
        {"query": "write a story about a cat"}
    ],
})

try:
    # stateless request to autogen server
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("response:", response.json())
except Exception as e:
    print("Error:", e)