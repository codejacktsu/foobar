import unittest
import distract


class MyTestCase(unittest.TestCase):
    def test_1(self):
        value = 10
        self.assertEqual(distract.solution(value), 89)
