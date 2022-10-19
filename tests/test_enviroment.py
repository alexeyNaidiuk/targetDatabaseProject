import os


from dotenv import load_dotenv
import unittest


load_dotenv()
TARGETS_FOLDER = os.environ.get('TARGET_FOLDER')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        self.assertIsNotNone(HOST)
        self.assertIsNotNone(PORT)
        self.assertIsNotNone(TARGETS_FOLDER)
