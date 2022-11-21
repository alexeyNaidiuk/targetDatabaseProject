import unittest
from threading import Thread

import requests

from app.config import HOST, PORT
from app.module.pools import TargetsFactory


class TestTargetRetrieve(unittest.TestCase):

    def test_turkey_reload(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 3278309')

    def test_alotof_reload(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/alotof/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 2556421')

    def test_dbru_reload(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/dbru/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 649671')

    def test_rub36_reload(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/rub36/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 75970')

    def test_mix_ru_reload(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/mixru/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 3295117')

    def test_clear_pool(self):
        for pool in TargetsFactory.pools.keys():
            requests.get(f'http://{HOST}:{PORT}/targets/{pool}/reload').content.decode()
            resp = requests.get(f'http://{HOST}:{PORT}/targets/{pool}/clear').content.decode()
            amount = requests.get(f'http://{HOST}:{PORT}/targets/{pool}/length').content.decode()
            self.assertEqual('target pool cleared', resp)
            self.assertEqual(0, int(amount))

    def test_get_target(self):
        for pool in TargetsFactory.pools.keys():
            requests.get(f'http://{HOST}:{PORT}/targets/{pool}/reload')
            value = requests.get(f'http://{HOST}:{PORT}/targets/{pool}/pop').content.decode()
            self.assertTrue('@' or '%' in value)

    def test_get_target_loop(self):
        def _check_method():
            requests.get(f'http://{HOST}:{PORT}/targets/turkey/pop')

        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()

        threads = []
        retrieved_amount = 100
        for _ in range(retrieved_amount):
            thread = Thread(target=_check_method)
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        threads.clear()

        amount = requests.get(f'http://{HOST}:{PORT}/targets/turkey/length').content.decode()
        self.assertEqual(int(amount), 3_278_309 - retrieved_amount)
