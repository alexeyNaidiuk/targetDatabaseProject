import unittest
from threading import Thread

import requests

from app.config import HOST, PORT
from app.module.pools import WwmixProxyFilePool, WestProxyFilePool, CheckedProxyFilePool, VladProxyFilePool, ParsedProxyFilePool


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

    def test_wwmix_proxies(self):
        url = f'http://{HOST}:{PORT}/proxies/wwmix/pool'
        pool = requests.get(url).text.splitlines()
        self.assertListEqual(WwmixProxyFilePool().get_pool(), pool)

        working = check_pool(pool, time_limit=10)
        print(len(working))
        self.assertNotEqual(working, [])

    def test_west_proxies(self):
        url = f'http://{HOST}:{PORT}/proxies/west/pool'
        pool = requests.get(url).text.splitlines()
        self.assertListEqual(WestProxyFilePool().get_pool(), pool)

        working = check_pool(pool, time_limit=10)
        print(len(working))
        self.assertNotEqual(working, [])

    def test_checked_proxies(self):
        url = f'http://{HOST}:{PORT}/proxies/checked/pool'
        pool = requests.get(url).text.splitlines()
        self.assertListEqual(CheckedProxyFilePool().get_pool(), pool)

        working = check_pool(pool, time_limit=10)
        print(len(working))
        self.assertNotEqual(working, [])

    def test_vlad_proxies(self):
        url = f'http://{HOST}:{PORT}/proxies/vlad/pool'
        pool = requests.get(url).text.splitlines()
        self.assertListEqual(VladProxyFilePool().get_pool(), pool)

        working = check_pool(pool, time_limit=15)
        print(len(working))
        self.assertNotEqual(working, [])

    def test_parsed_proxies(self):
        url = f'http://{HOST}:{PORT}/proxies/parsed/pool'
        pool = requests.get(url).text.splitlines()
        self.assertListEqual(ParsedProxyFilePool().get_pool(), pool)

        working = check_pool(pool, time_limit=10)
        print(len(working))
        self.assertNotEqual(working, [])
