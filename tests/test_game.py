# unit tests for the main module
import unittest

from src import Game

class TestGame(unittest.TestCase):
    def test_main(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()