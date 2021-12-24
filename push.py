import requests
import json

YOUR_TOKEN = '4979bff4c2a77b2f4dfe1943a4af56239e687a48'
YOUR_APP_ID = '5ej19744zxjl9n3e'

url = f'https://api.pushe.co/v2/messaging/web-rapid/'

headers = {
    'Authorization': f'Token {YOUR_TOKEN}',
    'Content-Type': 'application/json'
}

payload = json.dumps({
    'app_id': YOUR_APP_ID,
    'data': {
        'title': 'this is Jesus',
        'content': 'Ok ostad'
    },
    'custom_content': {
        'key1': 'value1',
        'key2': 'value2'
    },
    'device_id': [
        'device_id_1', 
        'device_id_2', 
    ]
})

r = requests.post(url, data=payload, headers=headers)

print(r.status_code)
