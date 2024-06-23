class QueueUsingStacks:
    """
    A queue implementation using two stacks.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else None

def validate_brackets(string):
    """
    Check if the brackets in the given string are balanced.
    Returns True if balanced, False otherwise.
    """

    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    stack = []
    
    for char in string:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return not stack

def next_greater_element(nums):
    """
    Given a list of numbers, for each element find the next greater element and return their list.
    If no greater element exists for an element, use -1 instead.
    """
    result = [-1] * len(nums)
    
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result

def reverse_stack(stack):
    """
    Reverse the given stack using only push and pop operations.
    The function should return the reversed stack.
    """
    auxiliary_stack = []
    
    while stack:
        auxiliary_stack.append(stack.pop())
    
    return auxiliary_stack