import unittest
from threading import Thread

import requests

from app.config import HOST, PORT
from app.module.pools import TargetsFactory


class TestTargetRetrieve(unittest.TestCase):

    def test_get_target(self):
        for pool in TargetsFactory.pools.keys():
            value = requests.get(f'http://{HOST}:{PORT}/targets/{pool}/pop').content.decode()
            self.assertTrue('@' or '%' in value)
