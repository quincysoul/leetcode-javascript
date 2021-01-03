import unittest
from ...howsum.recursive import Solution


class Test(unittest.TestCase):
    def test_expected_alvins(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([4, 3], solution.recursive_howsum(7, [5, 3, 4, 7]))

    def test_expected_alvins_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([4, 3], solution.recursive_howsum(7, [5, 3, 4, 7]))

    def test_expected_alvins_3(self):
        "Should return False."
        solution = Solution()
        self.assertEqual(None, solution.recursive_howsum(7, [2, 4]))

    def test_expected(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([10], solution.recursive_howsum(10, [10]))

    def test_expected_1(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual([5, 5], solution.recursive_howsum(10, [5, 5]))

    def test_expected_2(self):
        "Should return True if possible."
        solution = Solution()
        self.assertEqual(
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            solution.recursive_howsum(100, [10, 90]),
        )

    # def test_expected_3(self):
    #     "Should return None if possible."
    #     solution = Solution()
    #     self.assertEqual(True, solution.recursive_howsum(300, [7, 14]))

