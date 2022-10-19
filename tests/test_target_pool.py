import unittest

from app.module import TurkeyTargetFilePool


class TestTargetPool(unittest.TestCase):
    def test_pop(self):
        pool = TurkeyTargetFilePool()
        target = pool.pop()
        self.assertEqual('Kiyajmp@gmail.com', target)

    def test_append(self):
        pool = TurkeyTargetFilePool()
        pool.append('softumwork@gmail.com')
        self.assertIn('softumwork@gmail.com', pool.pool)

    def test_clear(self):
        pool = TurkeyTargetFilePool()
        pool.clear()
        self.assertEqual([], pool.pool)

    def test_reload(self):
        pool = TurkeyTargetFilePool()
        pool.clear()
        pool.reload()
        self.assertNotEqual([], pool.pool)
