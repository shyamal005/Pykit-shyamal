

import unittest
import time
from pykit import decorators

class TestDecorators(unittest.TestCase):

    def test_memoize(self):
        call_count = 0

        @decorators.memoize
        def slow_function(x):
            nonlocal call_count
            call_count += 1
            time.sleep(0.01)  # Simulate work
            return x * 2

        # First call should be slow and increment count
        self.assertEqual(slow_function(5), 10)
        self.assertEqual(call_count, 1)

        # Second call with same arg should be fast and not increment count
        self.assertEqual(slow_function(5), 10)
        self.assertEqual(call_count, 1)

        # Call with different arg should be slow and increment count
        self.assertEqual(slow_function(10), 20)
        self.assertEqual(call_count, 2)

    def test_retry(self):
        fail_count = 0

        @decorators.retry(tries=3, delay=0.01)
        def sometimes_fail():
            nonlocal fail_count
            if fail_count < 2:
                fail_count += 1
                raise ValueError("Temporary failure")
            return "Success"

        self.assertEqual(sometimes_fail(), "Success")
        self.assertEqual(fail_count, 2)

        @decorators.retry(tries=3, delay=0.01)
        def always_fail():
            raise ConnectionError("Service unavailable")

        with self.assertRaises(ConnectionError):
            always_fail()

if __name__ == '__main__':
    unittest.main()