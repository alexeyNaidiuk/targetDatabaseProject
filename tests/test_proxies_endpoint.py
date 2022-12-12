import unittest
from threading import Thread

import requests

from app.config import PORT
from app.module.pools import factories


def check_pool(proxy_pool, time_limit: int | None = None) -> list:
    working = []
    threads = []

    def check_proxy(proxy):
        proxies = {'http': proxy, 'https': proxy}
        try:
            response = requests.get('https://api.ipify.org', proxies=proxies, timeout=time_limit)
            if response.ok:
                print(proxy)
                working.append(proxy)
        except:
            pass

    for p in proxy_pool:
        t = Thread(target=check_proxy, args=(p,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    return working


class TestProxiesEndpoint(unittest.TestCase):

    def test_proxies(self):
        for pool_name, pool_instance in factories['proxies'].items():
            url = f'http://localhost:{PORT}/proxies/{pool_name}/pool'
            pool = requests.get(url).text.splitlines()
            self.assertListEqual(pool_instance.get_pool(), pool)
