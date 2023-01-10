import unittest
from threading import Thread
from typing import Iterable

import requests

from app.config import PORT
from app.module.pools import factories


def check_pool(proxy_pool: Iterable, time_limit: int | None = None) -> list:
    working = []
    threads = []

    def check_proxy(proxy):
        proxies = {'http': proxy, 'https': proxy}
        try:
            response = requests.get('http://ip-api.com/json/?fields=8217', proxies=proxies, timeout=time_limit)
            ip = response.json()['query']
            print(ip)
            working.append(proxy)
        except Exception as error:
            print(error)

    for p in proxy_pool:
        t = Thread(target=check_proxy, args=(p,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    return working


class TestProxiesEndpoint(unittest.TestCase):

    def test_all_proxies(self):
        for pool_name, pool_instance in factories['proxies'].items():
            url = f'http://localhost:{PORT}/proxies/{pool_name}/pool'
            pool = requests.get(url).text.splitlines()
            self.assertListEqual(pool_instance.get_pool(), pool)

    def test_west_proxy_pool(self):
        pool_name = 'west'
        url = f'http://localhost:{PORT}/proxies/{pool_name}/pool'
        pool: list = requests.get(url).text.splitlines()
        print(check_pool(pool))
