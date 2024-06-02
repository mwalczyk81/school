def find_max_min(numbers):
    """
    Find the maximum and minimum numbers in a list.
    Return them as a tuple (max, min).
    """
    if not numbers:
        return None, None
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

def check_symmetry(string):
    """
    Check if the given string is symmetrical.
    Return True if it is, False otherwise.
    """
    return string == string[::-1]

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    Return the merged sorted list.
    """
    return sorted(list1 + list2)

def sum_of_squares(nums):
    """
    Calculate and return the sum of squares of the numbers in the list.
    """
    return sum(x ** 2 for x in nums)

def string_reversal(s):
    """
    Reverse the given string and return it.
    """
    return s[::-1]

def find_second_largest(nums):
    """
    Find and return the second largest number in the list.
    If the list is too short, return None.
    """
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for n in nums:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second if second != float('-inf') else None
