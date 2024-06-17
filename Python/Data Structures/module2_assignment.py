def array_sum(arr):
    """
    Calculate and return the sum of elements in an array 'arr'.
    """
    total = 0
    for element in arr:
        total += element
    return total

def find_middle_node(linked_list):
    """
    Find and return the middle node of a singly linked list.
    If the list has an even number of nodes, return the second middle node.
    """
    slow = linked_list
    fast = linked_list
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

def remove_duplicates_from_sorted_array(arr):
    """
    Given a sorted array, remove the duplicates in-place such that each element appears only once.
    Return the new length of the array.
    """
    if not arr:
        return 0
    
    j = 0
    
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return j + 1

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next