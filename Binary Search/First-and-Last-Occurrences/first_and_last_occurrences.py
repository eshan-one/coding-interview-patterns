"""
Problem: First and Last Occurrences of a Number

Problem Statement:
Given an array of integers sorted in non-decreasing order, return the first and 
last indexes of a target number. If the target is not found, return [-1, -1].

Example 1:
    Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
    Output: [3, 5]
    Explanation: The first and last occurrences of number 4 are at indexes 3 and 5.

========================================
APPROACH EXPLANATION:
========================================
Since the array is sorted, we can use binary search to efficiently find both the 
first and last occurrences of the target number. We'll perform two binary searches:

1. FIND FIRST OCCURRENCE (leftmost position):
   - Modified binary search that continues searching left even when target is found
   - When we find the target, we move left to look for earlier occurrences
   - The leftmost value that equals target is our first occurrence

2. FIND LAST OCCURRENCE (rightmost position):
   - Modified binary search that continues searching right when target is found
   - When we find the target, we move right to look for later occurrences
   - The rightmost value that equals target is our last occurrence

========================================
TIME COMPLEXITY: O(log n)
========================================
- We perform TWO binary searches (finding first and last occurrences)
- Each binary search: O(log n) time
- Total: O(log n) + O(log n) = O(log n)

Why O(log n)? Because we eliminate half of the remaining elements in each iteration.
Even though we search twice, it's still O(log n) because constants don't affect Big-O.

========================================
SPACE COMPLEXITY: O(1)
========================================
- We only use a constant amount of extra space (pointers like left, right, mid)
- No additional data structures that scale with input size
- The space used doesn't depend on the input size

========================================
DRY ITERATION (WALKTHROUGH):
========================================
Let's trace through with:
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 4
    Array indices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

--- FINDING FIRST OCCURRENCE OF 4 ---

Iteration 1:
    left = 0, right = 12
    mid = (0 + 12) // 2 = 6
    nums[6] = 5
    5 > 4, so move right: right = 5

Iteration 2:
    left = 0, right = 5
    mid = (0 + 5) // 2 = 2
    nums[2] = 3
    3 < 4, so move left: left = 3

Iteration 3:
    left = 3, right = 5
    mid = (3 + 5) // 2 = 4
    nums[4] = 4 ✓ FOUND TARGET, but continue searching left
    right = 3  (move right pointer to mid - 1)

Iteration 4:
    left = 3, right = 3
    mid = (3 + 3) // 2 = 3
    nums[3] = 4 ✓ FOUND TARGET, and this is leftmost
    right = 2  (move right pointer to mid - 1)

Iteration 5:
    left = 3, right = 2
    Loop ends (left > right)

Result: First occurrence at index 3 ✓

--- FINDING LAST OCCURRENCE OF 4 ---

Iteration 1:
    left = 0, right = 12
    mid = (0 + 12) // 2 = 6
    nums[6] = 5
    5 > 4, so move right: right = 5

Iteration 2:
    left = 0, right = 5
    mid = (0 + 5) // 2 = 2
    nums[2] = 3
    3 < 4, so move left: left = 3

Iteration 3:
    left = 3, right = 5
    mid = (3 + 5) // 2 = 4
    nums[4] = 4 ✓ FOUND TARGET, but continue searching right
    left = 5  (move left pointer to mid + 1)

Iteration 4:
    left = 5, right = 5
    mid = (5 + 5) // 2 = 5
    nums[5] = 4 ✓ FOUND TARGET, and this is rightmost
    left = 6  (move left pointer to mid + 1)

Iteration 5:
    left = 6, right = 5
    Loop ends (left > right)

Result: Last occurrence at index 5 ✓

FINAL ANSWER: [3, 5]

"""


def searchRange(nums, target):
    """
    Find the first and last occurrence of the target number in a sorted array.
    
    Args:
        nums (list[int]): A sorted array of integers
        target (int): The target number to search for
    
    Returns:
        list[int]: [first_index, last_index] or [-1, -1] if not found
    """
    if not nums:
        return [-1, -1]
    
    # Helper function to find the first/leftmost occurrence
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Helper function to find the last/rightmost occurrence
    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    first = findFirst(nums, target)
    
    # If first occurrence not found, return [-1, -1]
    if first == -1:
        return [-1, -1]
    
    last = findLast(nums, target)
    return [first, last]


# ========================================
# TEST CASES
# ========================================

def test_searchRange():
    """Test cases for the searchRange function"""
    
    # Test Case 1: Target appears multiple times
    nums1 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    assert searchRange(nums1, 4) == [3, 5], "Test Case 1 Failed"
    print("✓ Test Case 1 Passed: Multiple occurrences")
    
    # Test Case 2: Target appears only once
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    assert searchRange(nums2, 5) == [4, 4], "Test Case 2 Failed"
    print("✓ Test Case 2 Passed: Single occurrence")
    
    # Test Case 3: Target not found
    nums3 = [1, 2, 3, 5, 6, 7]
    assert searchRange(nums3, 4) == [-1, -1], "Test Case 3 Failed"
    print("✓ Test Case 3 Passed: Target not found")
    
    # Test Case 4: Target at the beginning
    nums4 = [4, 4, 4, 5, 6, 7]
    assert searchRange(nums4, 4) == [0, 2], "Test Case 4 Failed"
    print("✓ Test Case 4 Passed: Target at beginning")
    
    # Test Case 5: Target at the end
    nums5 = [1, 2, 3, 4, 4, 4]
    assert searchRange(nums5, 4) == [3, 5], "Test Case 5 Failed"
    print("✓ Test Case 5 Passed: Target at end")
    
    # Test Case 6: Empty array
    nums6 = []
    assert searchRange(nums6, 4) == [-1, -1], "Test Case 6 Failed"
    print("✓ Test Case 6 Passed: Empty array")
    
    # Test Case 7: Single element array - found
    nums7 = [5]
    assert searchRange(nums7, 5) == [0, 0], "Test Case 7 Failed"
    print("✓ Test Case 7 Passed: Single element - found")
    
    # Test Case 8: Single element array - not found
    nums8 = [5]
    assert searchRange(nums8, 3) == [-1, -1], "Test Case 8 Failed"
    print("✓ Test Case 8 Passed: Single element - not found")
    
    # Test Case 9: All elements are the target
    nums9 = [4, 4, 4, 4, 4]
    assert searchRange(nums9, 4) == [0, 4], "Test Case 9 Failed"
    print("✓ Test Case 9 Passed: All elements are target")
    
    # Test Case 10: Large array
    nums10 = list(range(1, 101)) + [100] * 50 + list(range(101, 151))
    assert searchRange(nums10, 100) == [99, 149], "Test Case 10 Failed"
    print("✓ Test Case 10 Passed: Large array")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    # Run tests
    test_searchRange()
    
    # Example usage
    print("\n" + "="*50)
    print("EXAMPLE USAGE:")
    print("="*50)
    
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 4
    result = searchRange(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Explanation: First occurrence at index {result[0]}, Last occurrence at index {result[1]}")
