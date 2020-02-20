
import unittest
import Guess


class TestMain(unittest.TestCase):

    def setUp(self):
        print("Run before every test!")

    def guess_game_too_low_value(self):
        test_value = 0
        result = Guess.guess_game(test_value)
        self.assertEqual(result, "Enter number between 1 -5!")

    def tearDown(self):
        print("Run after every test!")


if __name__ == "__main__":
    unittest.main()
