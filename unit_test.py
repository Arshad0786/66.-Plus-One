import unittest
from PlusOne_Dev import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = [1, 2, 3]
        self.assertEqual(temp.plusOne(self.input), [1, 2, 4])

    def test_empty_list(self):
        temp = Solution()
        self.input = []
        self.assertEqual(temp.plusOne(self.input), None)

    def test_one_digit(self):
        temp = Solution()
        self.input = [1]
        self.assertEqual(temp.plusOne(self.input), [2])

    def test_one_digit_with_carry(self):
        temp = Solution()
        self.input = [9]
        self.assertEqual(temp.plusOne(self.input), [1, 0])

    def test_long_digits(self):
        temp = Solution()
        self.input = [9, 7, 2, 3, 4, 5, 6, 8, 4, 4, 4, 4, 7, 4, 8]
        self.assertEqual(temp.plusOne(self.input), [
                         9, 7, 2, 3, 4, 5, 6, 8, 4, 4, 4, 4, 7, 4, 9])

    def test_long_digits_all_carry(self):
        temp = Solution()
        self.input = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        self.assertEqual(temp.plusOne(self.input), [
                         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
