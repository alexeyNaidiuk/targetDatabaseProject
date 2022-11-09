import unittest

from app.module import TurkeyTargetFilePool, RussianTargetFilePool, RussianDbrTargetFilePool


class TestTurkeyTargetPool(unittest.TestCase):
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


class TestRussianTargetPool(unittest.TestCase):
    def test_pop(self):
        pool = RussianTargetFilePool()
        target = pool.pop()
        self.assertEqual('zajkowy111@o2.pl', target)

    def test_append(self):
        pool = RussianTargetFilePool()
        pool.append('softumwork@gmail.com')
        self.assertIn('softumwork@gmail.com', pool.pool)

    def test_clear(self):
        pool = RussianTargetFilePool()
        pool.clear()
        self.assertEqual([], pool.pool)

    def test_reload(self):
        pool = RussianTargetFilePool()
        pool.clear()
        pool.reload()
        self.assertNotEqual([], pool.pool)


class TestRussianDbrTargetPool(unittest.TestCase):
    def test_pop(self):
        pool = RussianDbrTargetFilePool()
        target = pool.pop()
        self.assertEqual('', target)

    def test_append(self):
        pool = RussianDbrTargetFilePool()
        pool.append('softumwork@gmail.com')
        self.assertIn('softumwork@gmail.com', pool.pool)

    def test_clear(self):
        pool = RussianDbrTargetFilePool()
        pool.clear()
        self.assertEqual([], pool.pool)

    def test_reload(self):
        pool = RussianDbrTargetFilePool()
        pool.clear()
        pool.reload()
        self.assertNotEqual([], pool.pool)
