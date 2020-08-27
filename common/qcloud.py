import requests
import time
import random
import hmac
import hashlib
import base64


class Qcloud:
    def __init__(self, id: str, key: str, domain: str):
        self.id = id
        self.key = key
        self.domain = domain

    def request(self, action: str, args: dict):
        url = 'cns.api.qcloud.com/v2/index.php'
        body = {
            'Action': action,
            'SecretId': self.id,
            'Timestamp': int(time.time()),
            'Nonce': int(random.uniform(1, 99999)),
            'SignatureMethod': 'HmacSHA256'
        }
        body.update(args)

        parameters = 'POST' + url + '?'
        for key in sorted(body):
            parameters += key + '=' + body[key] + '&'

        body['Signature'] = base64.b64encode(hmac.new(
            self.key.encode('utf-8'),
            parameters[0: -1].encode('utf-8'),
            hashlib.sha256
        ).digest())

        return requests.post(
            url='https://' + url,
            data=body
        )

    def resolve(self, sub_domain: str, record: str, ttl: int) -> bool:
        response = self.request('RecordList', {
            'domain': self.domain,
            'subDomain': sub_domain,
        })
        result = response.json()
        if result['code'] != 0:
            return False
        if len(result['data']['records']) != 0:
            response = self.request('RecordModify', {
                'domain': self.domain,
                'recordId': result['data']['records'][0]['id'],
                'subDomain': sub_domain,
                'recordType': 'TXT',
                'recordLine': '默认',
                'value': record,
                'ttl': ttl
            })
        else:
            response = self.request('RecordCreate', {
                'domain': self.domain,
                'subDomain': sub_domain,
                'recordType': 'TXT',
                'recordLine': '默认',
                'value': record,
                'ttl': ttl
            })

        result = response.json()
        if result['code'] != 0:
            return False
        return True
