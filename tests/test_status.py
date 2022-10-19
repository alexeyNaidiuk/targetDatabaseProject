import os
import unittest

import requests
from dotenv import load_dotenv
import json


load_dotenv()


class TestStatus(unittest.TestCase):

    def test_status(self):
        response = requests.get(f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}')
        content = json.loads(response.content.decode())
        self.assertEqual(content, {'status': 'ok'})
