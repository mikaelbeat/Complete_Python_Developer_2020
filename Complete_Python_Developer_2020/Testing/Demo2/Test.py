
import unittest
import Main

# All unittests are run with command
# python3 -m unittest -v

class TestMain(unittest.TestCase):

    def setUp(self):
        print("Run before every test!")

    def test_demo_function_int(self):
        test_value1 = 10
        test_value2 = 10
        result = Main.demo_function(test_value1, test_value2)
        self.assertEqual(result, 20)

    def test_demo_function_string(self):
        test_value1 = 10
        test_value2 = "Hello"
        result = Main.demo_function(test_value1, test_value2)
        self.assertIsInstance(result, TypeError)

 

    def tearDown(self):
        print("Run after every test!")


if __name__ == "__main__":
    unittest.main()
