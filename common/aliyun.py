from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import json


class Aliyun:
    def __init__(self, id: str, key: str, domain: str):
        self.id = id
        self.key = key
        self.domain = domain

    def resolve(self, sub_domain: str, record: str, ttl: int) -> bool:
        try:
            client = AcsClient(self.id, self.key)
            request = DescribeDomainRecordsRequest()
            request.set_DomainName(self.domain)
            request.set_RRKeyWord(sub_domain)
            request.set_accept_format('json')
            response = client.do_action_with_exception(request)
            result = json.loads(response)
            if result['TotalCount'] != 0:
                request = UpdateDomainRecordRequest()
                request.set_RecordId(result['DomainRecords']['Record'][0]['RecordId'])
                request.set_RR(sub_domain)
                request.set_Type('TXT')
                request.set_Value(record)
                request.set_TTL(ttl)
                request.set_accept_format('json')
                client.do_action_with_exception(request)
            else:
                request = AddDomainRecordRequest()
                request.set_DomainName(self.domain)
                request.set_RR(sub_domain)
                request.set_Type('TXT')
                request.set_Value(record)
                request.set_TTL(ttl)
                request.set_accept_format('json')
                client.do_action_with_exception(request)
            return True
        except Exception as e:
            print(e)
            return False
