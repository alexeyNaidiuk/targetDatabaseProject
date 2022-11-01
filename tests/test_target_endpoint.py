import unittest
from threading import Thread

import requests

from app.config import HOST, PORT


class TestTurkeyTargetRetrieve(unittest.TestCase):

    def test_reload_pool(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 3278309')

    def test_get_amount(self):
        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()
        amount = requests.get(f'http://{HOST}:{PORT}/targets/turkey/amount').content.decode()
        self.assertEqual(int(amount), 3_278_309)

    def test_clear_pool(self):
        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()
        resp = requests.get(f'http://{HOST}:{PORT}/targets/turkey/clear').content.decode()
        amount = requests.get(f'http://{HOST}:{PORT}/targets/turkey/amount').content.decode()
        self.assertEqual('target pool cleared', resp)
        self.assertEqual(0, int(amount))

    def test_get_target(self):
        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload')
        value = requests.get(f'http://{HOST}:{PORT}/targets/turkey/random').content.decode()
        self.assertEqual('Kiyajmp@gmail.com', value)

    def test_append_to_pool(self):
        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload')
        append_target = 'softumwork@gmail.com'
        requests.post(f'http://{HOST}:{PORT}/targets/turkey/append', json={'email': append_target})
        value = requests.get(f'http://{HOST}:{PORT}/targets/turkey/random').content.decode()
        self.assertEqual(append_target, value)

    def test_get_target_loop(self):
        def _check_method():
            response = requests.get(f'http://{HOST}:{PORT}/targets/turkey/random')
            value = response.content.decode()

            response = requests.post(f'http://{HOST}:{PORT}/targets/turkey/append', json={'email': value})
            value = response.content.decode()
            return value

        requests.get(f'http://{HOST}:{PORT}/targets/turkey/reload').content.decode()

        threads = []
        for _ in range(1000):
            thread = Thread(target=_check_method)
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        threads.clear()

        amount = requests.get(f'http://{HOST}:{PORT}/targets/turkey/amount').content.decode()
        self.assertEqual(int(amount), 3_278_309)


class TestRussianTargetRetrieve(unittest.TestCase):

    def test_reload_pool(self):
        content = requests.get(f'http://{HOST}:{PORT}/targets/russian/reload').content.decode()
        self.assertEqual(content, 'reloaded! current amount is 2556423')

    def test_get_amount(self):
        requests.get(f'http://{HOST}:{PORT}/targets/russian/reload').content.decode()
        amount = requests.get(f'http://{HOST}:{PORT}/targets/russian/amount').content.decode()
        self.assertEqual(int(amount), 2556423)

    def test_clear_pool(self):
        requests.get(f'http://{HOST}:{PORT}/targets/russian/reload').content.decode()
        resp = requests.get(f'http://{HOST}:{PORT}/targets/russian/clear').content.decode()
        amount = requests.get(f'http://{HOST}:{PORT}/targets/russian/amount').content.decode()
        self.assertEqual('target pool cleared', resp)
        self.assertEqual(0, int(amount))

    def test_get_target(self):
        requests.get(f'http://{HOST}:{PORT}/targets/russian/reload')
        value = requests.get(f'http://{HOST}:{PORT}/targets/russian/random').content.decode()
        self.assertEqual('zajkowy111@o2.pl', value)

    def test_append_to_pool(self):
        requests.get(f'http://{HOST}:{PORT}/targets/russian/reload')
        append_target = 'softumwork@gmail.com'
        requests.post(f'http://{HOST}:{PORT}/targets/russian/append', json={'email': append_target})
        value = requests.get(f'http://{HOST}:{PORT}/targets/russian/random').content.decode()
        self.assertEqual(append_target, value)

    def test_get_target_loop(self):

        def _check_method():
            response = requests.get(f'http://{HOST}:{PORT}/targets/russian/random')
            value = response.content.decode()

            response = requests.post(f'http://{HOST}:{PORT}/targets/russian/append', json={'email': value})
            value = response.content.decode()
            return value

        requests.get(f'http://{HOST}:{PORT}/targets/russian/reload').content.decode()

        threads = []
        for _ in range(1000):
            thread = Thread(target=_check_method)
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        threads.clear()

        amount = requests.get(f'http://{HOST}:{PORT}/targets/russian/amount').content.decode()
        self.assertEqual(int(amount), 2556423)
