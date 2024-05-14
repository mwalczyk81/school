def selection_sort(nums):
    """
    Implement the selection sort algorithm to sort the list 'nums' in ascending order.
    Return the sorted list.
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

def quick_sort(arr):
    """
    Implement the quick sort algorithm to sort the list 'arr' in ascending order.
    Return the sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def binary_search_first_occurrence(arr, x):
    """
    Implement a variation of binary search to find the first occurrence of 'x' in the sorted list 'arr'.
    Return the index of the first occurrence of 'x'. If 'x' is not present in 'arr', return -1.
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

