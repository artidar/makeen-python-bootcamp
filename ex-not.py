
import requests
import re
from random import randint
import qrcode
import os





api_key = '4979bff4c2a77b2f4dfe1943a4af56239e687a48'
push = 'https://api.pushe.co/v2/messaging/notifications/'
upload = 'https://api.pushe.co/v2/files/icons/'
app_id = '5ej19744zxjl9n3e'


class Notification:
    api_key = os.environ.get('pi_key')

    push = os.environ.get('push')

    upload = os.environ.get('upload')

    app_id = os.environ.get('app_id')

    pattern = '^[A-Z][a-z]+\s[A-Z][a-z]+$'
    
    
    
    headers = {'Authorization': f'Token {api_key}'}

    

    def inf_user(self):
        name = input('Enter your name like this ---> Kashayar Artidar : ')
        if re.match(Notification.pattern, name):
            self.name = name
            self.username = self.name.replace(' ', '.').lower()
            self.user_id = randint(1000, 9999)
            self.userinfo = self.username + '.jpeg'
        else:
            print('Wrong Input - Try again accoirding to pattern example: Kashayar Artidar')
            self.inf_user()

    def make_qrcode(self):
        img = qrcode.make(f'name: {self.name}\nusername: {self.username}\nid: {self.user_id}')
        img.save(f'{self.userinfo}')



    def upload_qrcode(self):
        files = ('image', (f'{self.userinfo}', open(f'{self.userinfo}','rb'),'image/jpeg'))

        response = requests.post(Notification.upload, headers=Notification.headers, files=files)
        return response.json().get("url", "")


    def push_notif(self):
        qrcode = self.upload_qrcode()
        data = {
            'app_ids': Notification.app_id,
            'data': {
                'title': 'QR code: ',
                'content': qrcode
            }
        }
        requests.post(Notification.push, json=data, headers=Notification.headers)

test = Notification()
test.inf_user()
test.make_qrcode()
test.upload_qrcode()
test.push_notif()






        

        
        

    