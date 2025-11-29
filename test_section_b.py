import unittest

from section_b import (
    is_even, max_of_three, count_vowels, sum_digits, reverse_string, 
    fibonacci, is_palindrome, first_duplicate, find_min_max, char_frequency,
    fizzbuzz, find_evens, remove_negatives, split_even_odd, merge_lists, 
    factorial, count_uppercase, only_digits, find_index, count_occurrences
)

class TestFunctions(unittest.TestCase):

    # Q1
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-4))

    # Q2
    def test_max_of_three(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(10, 5, 10), 10)
        self.assertEqual(max_of_three(-1, -2, -3), -1)

    # Q3
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("AeIoU"), 5)

    # Q4
    def test_sum_digits(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(9999), 36)

    # Q5
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

    # Q6
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    # Q7
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))
        self.assertFalse(is_palindrome("hello"))

    # Q8
    def test_first_duplicate(self):
        self.assertEqual(first_duplicate([1,2,3,2,4]), 2)
        self.assertEqual(first_duplicate([1,2,3]), None)
        self.assertEqual(first_duplicate([]), None)
        self.assertEqual(first_duplicate([5,5,5]), 5)

    # Q9
    def test_find_min_max(self):
        self.assertEqual(find_min_max([1,2,3,4]), (1,4))
        self.assertEqual(find_min_max([7]), (7,7))
        self.assertEqual(find_min_max([-1,-5,0]), (-5,0))

    # Q10
    def test_char_frequency(self):
        self.assertEqual(char_frequency("aab"), {'a':2,'b':1})
        self.assertEqual(char_frequency(""), {})
        self.assertEqual(char_frequency("abcabc"), {'a':2,'b':2,'c':2})

    # Q11
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(5), [1,2,"Fizz",4,"Buzz"])
        self.assertEqual(fizzbuzz(15)[-1], "FizzBuzz")
        self.assertEqual(fizzbuzz(3), [1,2,"Fizz"])

    # Q12
    def test_find_evens(self):
        self.assertEqual(find_evens([1,2,3,4,5]), [2,4])
        self.assertEqual(find_evens([1,3,5]), [])
        self.assertEqual(find_evens([]), [])

    # Q13
    def test_remove_negatives(self):
        self.assertEqual(remove_negatives([1,-2,3,-4,0]), [1,3,0])
        self.assertEqual(remove_negatives([-1,-2]), [])
        self.assertEqual(remove_negatives([]), [])

    # Q14
    def test_split_even_odd(self):
        self.assertEqual(split_even_odd([1,2,3,4]), ([2,4],[1,3]))
        self.assertEqual(split_even_odd([0,0,1]), ([0,0],[1]))
        self.assertEqual(split_even_odd([]), ([],[]))

    # Q15
    def test_merge_lists(self):
        a = [1,2]
        b = [3,4]
        merged = merge_lists(a,b)
        self.assertEqual(merged, [1,2,3,4])
        self.assertEqual(a, [1,2])  # original a unchanged

    # Q16
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    # Q17
    def test_count_uppercase(self):
        self.assertEqual(count_uppercase("HelloWorld"), 2)
        self.assertEqual(count_uppercase("HELLO"), 5)
        self.assertEqual(count_uppercase("hello"), 0)

    # Q18
    def test_only_digits(self):
        self.assertTrue(only_digits("12345"))
        self.assertFalse(only_digits("12a34"))
        self.assertFalse(only_digits(""))

    # Q19
    def test_find_index(self):
        self.assertEqual(find_index([1,2,3],2), 1)
        self.assertEqual(find_index([1,2,3],4), -1)
        self.assertEqual(find_index([],1), -1)

    # Q20
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1,2,1,3],1), 2)
        self.assertEqual(count_occurrences([],1), 0)
        self.assertEqual(count_occurrences([0,0,0],0), 3)

if __name__ == "__main__":
    unittest.main()
