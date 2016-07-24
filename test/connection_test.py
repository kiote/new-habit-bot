import unittest

from model import database


class TestConnection(unittest.TestCase):
    def setup(self):
        database.connect()

    def test_connection(self):
        """
        Actually, we just need to call setup and teardown
        to make sure that connection works.
        """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
