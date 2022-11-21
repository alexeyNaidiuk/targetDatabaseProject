import unittest

import requests

from app.config import HOST, PORT
from app.module.pools import WwmixProxyFilePool


class TestProxiesEndpoint(unittest.TestCase):

    def test_pool(self):
        url = f'http://{HOST}:{PORT}/proxies/wwmix/pool'
        response = requests.get(url)
        value = response.content.decode()
        self.assertListEqual(WwmixProxyFilePool().pool, value.split('\n'))
