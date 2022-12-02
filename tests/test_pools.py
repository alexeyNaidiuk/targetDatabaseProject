import unittest

from app.module.pools import TargetsFactory


class TestTargetPool(unittest.TestCase):

    def test_pop(self):
        for pool in TargetsFactory.pools.values():
            target = pool.pop()
            self.assertTrue('@' or '%' in target)

    def test_clear(self):
        for pool in TargetsFactory.pools.values():
            pool._clear()
            self.assertEqual([], pool.pool)

    def test_reload(self):
        for pool in TargetsFactory.pools.values():
            pool._clear()
            pool._reload()
            self.assertNotEqual([], pool.pool)
