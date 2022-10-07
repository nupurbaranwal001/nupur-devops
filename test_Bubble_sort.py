from unittest import TestCase
from Bubble_sort import *


class Test(TestCase):
    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubbleSort([5, 5, 7, 8, 2, 4, 1]), [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_negative_numbers_only(self):
        self.assertEqual(bubbleSort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(bubbleSort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_same_numbers(self):
        self.assertEqual(bubbleSort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubbleSort([]), [])
