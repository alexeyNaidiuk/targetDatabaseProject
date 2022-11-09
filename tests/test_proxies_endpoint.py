import unittest

import requests

from app.config import HOST, PORT
from app.module import WwmixProxyFilePool, WestProxyFilePool


class TestWwmixProxies(unittest.TestCase):

    def test_pool(self):
        url = f'http://{HOST}:{PORT}/proxies/wwmix'
        response = requests.get(url)
        value = response.content.decode()
        self.assertListEqual(WwmixProxyFilePool().pool, value.split('\n'))


class TestWestProxies(unittest.TestCase):

    def test_pool(self):
        url = f'http://{HOST}:{PORT}/proxies/west'
        response = requests.get(url)
        value = response.content.decode()
        self.assertListEqual(WestProxyFilePool().pool, value.split('\n'))
