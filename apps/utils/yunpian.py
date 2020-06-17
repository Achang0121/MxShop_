import json

import requests


class YunPian:
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"
    
    def send_sms(self, code, mobile):
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': f"【常加明Test】您的验证码是{code}。如非本人操作，请忽略本短信"
        }
        response = requests.post(self.single_send_url, data=params)
        res_dict = json.loads(response.text)
        return res_dict
