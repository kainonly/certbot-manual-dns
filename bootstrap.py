#!/usr/bin/python3
import configparser
import common
import os
import time

CERTBOT_DOMAIN = os.environ['CERTBOT_DOMAIN']
CERTBOT_VALIDATION = os.environ['CERTBOT_VALIDATION']

try:
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    if cfg.has_section(CERTBOT_DOMAIN) is False:
        raise Exception(f'The domain [{CERTBOT_DOMAIN}] does not exist in the configuration')

    option = cfg[CERTBOT_DOMAIN]
    if option.get('platform') is None:
        raise Exception(f'Please configure the [platform] for the domain [{CERTBOT_DOMAIN}]')
    platform = option.get('platform')
    if option.get('id') is None:
        raise Exception(f'Please configure the [id] for the domain [{CERTBOT_DOMAIN}]')
    id = option.get('id')
    if option.get('key') is None:
        raise Exception(f'Please configure the [key] for the domain [{CERTBOT_DOMAIN}]')
    key = option.get('key')

    if platform == 'qcloud':
        dns = common.Qcloud(id, key, CERTBOT_DOMAIN)
    else:
        raise Exception(f'The domain [{CERTBOT_DOMAIN}] platform service provider does not support')
    dns.resolve('_acme-challenge', CERTBOT_VALIDATION, option.get('ttl') or 600)
    time.sleep(3)
    print(f'Verify that the record [_acme-challenge.{CERTBOT_DOMAIN}] is parsed successfully')
except Exception as e:
    raise
