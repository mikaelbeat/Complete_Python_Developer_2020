
import unittest
import Main

# All unittests are run with command
# python3 -m unittest -v

class TestMain(unittest.TestCase):

    def setUp(self):
        print("Run before every test!")

    def test_demo_function_int(self):
        test_value = 10
        result = Main.demo_function(test_value)
        self.assertEqual(result, 15)

    def test_demo_function_string(self):
        test_value = "TEST"
        result = Main.demo_function(test_value)
        self.assertIsInstance(result, TypeError)

    def test_demo_function_None(self):
        test_value = None
        result = Main.demo_function(test_value)
        self.assertIsInstance(result, TypeError)

    def tearDown(self):
        print("Run after every test!")


if __name__ == "__main__":
    unittest.main()
