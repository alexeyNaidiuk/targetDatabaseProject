import json
import unittest

import requests

from app.config import HOST, PORT


class TestStatus(unittest.TestCase):

    def test_status(self):
        response = requests.get(f'http://{HOST}:{PORT}')
        content = json.loads(response.content.decode())
        self.assertEqual(content, {'status': 'ok'})
