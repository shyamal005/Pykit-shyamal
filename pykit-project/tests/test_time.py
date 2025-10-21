

import unittest
from datetime import datetime, timedelta
from pykit import time

class TestTime(unittest.TestCase):

    def test_parse_date(self):
        expected = datetime(2024, 10, 25)
        self.assertEqual(time.parse_date("2024-10-25"), expected)
        self.assertEqual(time.parse_date("10/25/2024"), expected)
        self.assertEqual(time.parse_date("October 25, 2024"), expected)
        with self.assertRaises(ValueError):
            time.parse_date("invalid date format")

    def test_humanize_delta(self):
        self.assertEqual(time.humanize_delta(timedelta(days=2, hours=5)), "2 days")
        self.assertEqual(time.humanize_delta(timedelta(days=1)), "1 day")
        self.assertEqual(time.humanize_delta(timedelta(hours=5)), "5 hours")
        self.assertEqual(time.humanize_delta(timedelta(minutes=45)), "45 minutes")
        self.assertEqual(time.humanize_delta(timedelta(seconds=30)), "30 seconds")
        self.assertEqual(time.humanize_delta(timedelta(seconds=1)), "1 second")

if __name__ == '__main__':
    unittest.main()