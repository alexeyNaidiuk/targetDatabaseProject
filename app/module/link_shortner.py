import logging

import requests

from app.config import ZENNO_KEY


URL = 'https://zennotasks.com/automation/api.php'
REFERALS = {
    'supercat': 'https://referencemen.live/ktVmDV?c=0098xLek_pT9MBd059d7cb95430c53',
    'luckybird': 'https://referencemen.live/ktVmDV?c=0097xLek_pT9MB5b4d7a1cbb052b1b',
    'allright': 'https://referencemen.live/ktVmDV?c=0114xLek_pT9MBc578b8a2b8d59856',
    'fortuneclock': 'https://referencemen.live/ktVmDV?c=0133xLek_pT9MB5ea167c052b0c66a'
}


def get_link(target_pool_name: str, referal_to_project: str) -> str:
    project_link = REFERALS[referal_to_project]

    if not referal_to_project:
        utm_campaign = target_pool_name
    else:
        utm_campaign = f'{target_pool_name}_{referal_to_project}'

    url = f'{project_link}&utm_campaign={utm_campaign}'
    params = {'key': ZENNO_KEY, 'shurl': url}
    response = requests.get(URL, params=params)
    content = response.text
    return content
