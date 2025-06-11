import unittest
from project1 import function_to_test

class TestProject1(unittest.TestCase):
    def test_function(self):
        self.assertEqual(function_to_test(args), expected_result)

if __name__ == '__main__':
    unittest.main()
