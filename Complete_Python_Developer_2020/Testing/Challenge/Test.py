
import unittest
import Guess


class TestMain(unittest.TestCase):

    def setUp(self):
        print("Run before every test!")

    def guess_game_correct_guess(self):
        random_value = 5
        guess = 5
        result = Guess.guess_game(random_value, guess)
        self.assertTrue(result)

    def guess_game_wrong_guess(self):
        result = Guess.guess_game(5, 0)
        self.assertFalse(result)

    def guess_game_invalid_number(self):
        result = Guess.guess_game(5, 11)
        self.assertFalse(result)

    def guess_game_invalid_input(self):
        result = Guess.guess_game(5, "11")
        self.assertFalse(result)

    def tearDown(self):
        print("Run after every test!")


if __name__ == "__main__":
    unittest.main()
