import unittest
import running


class MyTestCase(unittest.TestCase):
    def test_1(self):
        value = [1,1]
        self.assertEqual(running.solution(value), 2)

    def test_2(self):
        value = [1, 7, 3, 21, 13, 19]
        self.assertEqual(running.solution(value), 0)

    # def test_3(self):
    #     value = [1, 7, 3, 21, 13, 19, 19]
    #     self.assertEqual(running.solution(value), 1)
