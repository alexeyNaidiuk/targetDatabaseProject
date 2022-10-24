import unittest

from app.config import HOST, PORT, TARGETS_FOLDER


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        self.assertIsNotNone(HOST)
        self.assertIsNotNone(PORT)
        self.assertIsNotNone(TARGETS_FOLDER)
