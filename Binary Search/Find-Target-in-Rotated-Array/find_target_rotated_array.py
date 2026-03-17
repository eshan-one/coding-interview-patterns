"""
Problem: Find the Target in a Rotated Sorted Array

Problem Statement:
A rotated sorted array is an array of numbers sorted in ascending order, in which
a portion of the array is moved from the beginning to the end.
For example, [3, 4, 5, 1, 2] is a rotation of [1, 2, 3, 4, 5].

Given a rotated sorted array of UNIQUE numbers, return the index of a target value.
If the target value is not present, return -1.

Example:
    Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
    Output: 2
    Explanation: The target value 1 is at index 2.

========================================
APPROACH EXPLANATION:
========================================
The key insight is that even though the array is rotated, ONE HALF is always sorted.

At any point in binary search:
1. Check which half (left or right) is properly sorted
2. Determine if target lies in the sorted half
3. If yes: search that half
4. If no: search the other half

Step-by-step Logic:
1. Use left and right pointers
2. Calculate mid = (left + right) // 2
3. If nums[mid] == target: return mid
4. Check which half is sorted:
   - If nums[left] <= nums[mid]: LEFT half is sorted
     - If target is in [nums[left], nums[mid]]: search left
     - Otherwise: search right
   - Else: RIGHT half is sorted
     - If target is in [nums[mid], nums[right]]: search right
     - Otherwise: search left

Why This Works:
- In a rotated sorted array, exactly one half is always sorted
- We use the sorted half to make intelligent decisions about where to search
- We avoid the rotation point automatically

========================================
TIME COMPLEXITY: O(log n)
========================================
- Binary search eliminates half of the elements in each iteration
- Depth of recursion: log n

========================================
SPACE COMPLEXITY: O(1)
========================================
- Only using pointers (left, right, mid) - constant extra space
- No additional data structures

========================================
DRY ITERATION (WALKTHROUGH):
========================================
Example: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1

Initial state:
    left = 0, right = 8
    [8, 9, |1, 2, 3, 4, 5, 6, 7|] rotated between index 1 and 2

Iteration 1:
    mid = (0 + 8) // 2 = 4
    nums[mid] = 3
    nums[left] = 8, nums[right] = 7
    
    nums[left] (8) > nums[mid] (3)?
    Yes! RIGHT half [3, 4, 5, 6, 7] is sorted
    
    Is target (1) in sorted right half [3, 7]? NO
    Search LEFT half
    left = 0, right = mid - 1 = 3

Iteration 2:
    left = 0, right = 3
    mid = (0 + 3) // 2 = 1
    nums[mid] = 9
    
    nums[left] (8) <= nums[mid] (9)?
    Yes! LEFT half [8, 9] is sorted
    
    Is target (1) in sorted left half [8, 9]? NO
    Search RIGHT half
    left = mid + 1 = 2, right = 3

Iteration 3:
    left = 2, right = 3
    mid = (2 + 3) // 2 = 2
    nums[mid] = 1
    
    nums[mid] == target? YES!
    Return mid = 2

========================================
"""


def find_target_in_rotated_array(nums, target):
    """
    Find the index of target in a rotated sorted array.
    
    Args:
        nums: List of unique integers (rotated sorted array)
        target: The value to find
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found the target
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        # LEFT half is sorted
        if nums[left] <= nums[mid]:
            # Check if target is in the sorted left half
            if nums[left] <= target < nums[mid]:
                # Target is in left half
                right = mid - 1
            else:
                # Target is in right half
                left = mid + 1
        
        # RIGHT half is sorted
        else:
            # Check if target is in the sorted right half
            if nums[mid] < target <= nums[right]:
                # Target is in right half
                left = mid + 1
            else:
                # Target is in left half
                right = mid - 1
    
    # Target not found
    return -1


# ========================================
# TEST CASES
# ========================================

if __name__ == "__main__":
    # Test case 1: Target in right rotated portion
    nums1 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target1 = 1
    result1 = find_target_in_rotated_array(nums1, target1)
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {result1} (Expected: 2)")
    print()
    
    # Test case 2: Target in left rotated portion
    nums2 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target2 = 8
    result2 = find_target_in_rotated_array(nums2, target2)
    print(f"Test 2: nums = {nums2}, target = {target2}")
    print(f"Output: {result2} (Expected: 0)")
    print()
    
    # Test case 3: Target at end
    nums3 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target3 = 7
    result3 = find_target_in_rotated_array(nums3, target3)
    print(f"Test 3: nums = {nums3}, target = {target3}")
    print(f"Output: {result3} (Expected: 8)")
    print()
    
    # Test case 4: Target not found
    nums4 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target4 = 10
    result4 = find_target_in_rotated_array(nums4, target4)
    print(f"Test 4: nums = {nums4}, target = {target4}")
    print(f"Output: {result4} (Expected: -1)")
    print()
    
    # Test case 5: Single element array
    nums5 = [1]
    target5 = 1
    result5 = find_target_in_rotated_array(nums5, target5)
    print(f"Test 5: nums = {nums5}, target = {target5}")
    print(f"Output: {result5} (Expected: 0)")
    print()
    
    # Test case 6: No rotation (already sorted)
    nums6 = [1, 2, 3, 4, 5]
    target6 = 3
    result6 = find_target_in_rotated_array(nums6, target6)
    print(f"Test 6: nums = {nums6}, target = {target6}")
    print(f"Output: {result6} (Expected: 2)")
    print()
    
    # Test case 7: Rotated array with two elements
    nums7 = [3, 1]
    target7 = 1
    result7 = find_target_in_rotated_array(nums7, target7)
    print(f"Test 7: nums = {nums7}, target = {target7}")
    print(f"Output: {result7} (Expected: 1)")
