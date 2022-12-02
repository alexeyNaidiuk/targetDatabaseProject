import unittest

import requests

from app.config import HOST, PORT
from app.module.pools import factories


class TestTargetRetrieve(unittest.TestCase):

    def test_get_target(self):
        targets = factories['targets'].keys()
        for pool in targets:
            value = requests.get(f'http://{HOST}:{PORT}/targets/{pool}/pop').content.decode()
            self.assertTrue('@' or '%' in value)
