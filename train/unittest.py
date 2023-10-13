import unittest

# Assume you have a simple class that you want to test
class MathOperations:
    def add(self, a, b):
        return a + b

# Now, let's write some tests for this class
class TestMathOperations(unittest.TestCase):

    # This method is called before each test method
    def setUp(self):
        print("Setting up for the test...")
        # You might initialize resources, set up connections, etc.

    # This method is called after each test method
    def tearDown(self):
        print("Tearing down after the test...")
        # You might clean up resources, close connections, etc.

    def test_add_positive_numbers(self):
        math = MathOperations()
        result = math.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        math = MathOperations()
        result = math.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        math = MathOperations()
        result = math.add(2, -3)
        self.assertEqual(result, -1)

# Run the tests
if __name__ == '__main__':
    unittest.main()
