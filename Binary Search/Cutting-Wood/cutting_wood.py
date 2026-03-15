"""
Problem: Cutting Wood

Problem Statement:
You are given an array representing the heights of trees, and an integer k 
representing the total length of wood that needs to be cut.

A woodcutting machine is set to a certain height H. The machine cuts off the 
top part of all trees taller than H, while trees shorter than H remain untouched. 
Determine the highest possible setting of the woodcutter (H) so that it cuts 
at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest tree 
in the array.

Example:
    Input: heights = [2, 6, 3, 8], k = 7
    Output: 3
    Explanation: At height 3, we cut from the two taller trees:
                 - Tree at height 6: (6 - 3) = 3 meters
                 - Tree at height 8: (8 - 3) = 5 meters
                 Total: 3 + 5 = 8 meters (>= 7) ✓
                 At height 4: (6-4) + (8-4) = 6 meters (< 7) ✗

========================================
APPROACH EXPLANATION:
========================================
This is a classic "Binary Search on the Answer" problem.

Key Insight: As the height H increases, the total amount of wood cut decreases.
This monotonic property allows us to use binary search.

Search Space: H ranges from 0 to max(heights)

Binary Search Strategy:
1. We search for the HIGHEST H where total_wood_cut >= k
2. Use left and right pointers to define search range
3. For each mid height, calculate total wood cut
4. If wood >= k: This H might be the answer, try higher (left = mid + 1)
5. If wood < k: H is too high, search lower (right = mid - 1)

Why Binary Search?
- Without binary search: O(n * max_height) - checking every possible height
- With binary search: O(n * log(max_height)) - much more efficient

========================================
TIME COMPLEXITY: O(n * log M)
========================================
Where:
  n = number of trees (size of heights array)
  M = maximum height in the array

- Binary search on height: O(log M) iterations
- For each iteration, we calculate wood cut by iterating through all trees: O(n)
- Total: O(n * log M)

Example: For 1000 trees with max height 1000:
  Standard approach: 1000 * 1000 = 1,000,000 operations
  Binary search: 1000 * log(1000) ≈ 1000 * 10 = 10,000 operations

========================================
SPACE COMPLEXITY: O(1)
========================================
- Only constant extra space for variables (left, right, mid, result)
- No additional data structures
- In-place computation of wood cut amount

========================================
DRY ITERATION (WALKTHROUGH):
========================================
Let's trace through with:
    heights = [2, 6, 3, 8]
    k = 7

Step 1: Initialize
    left = 0
    right = max(heights) = 8
    result = 0 (default answer if no valid H found)

Step 2: Binary Search Loop

Iteration 1:
    left = 0, right = 8
    mid = (0 + 8) // 2 = 4
    
    Calculate wood cut at height 4:
      - Tree 0: 2 < 4, no cut
      - Tree 1: 6 > 4, cut (6 - 4) = 2
      - Tree 2: 3 < 4, no cut
      - Tree 3: 8 > 4, cut (8 - 4) = 4
      Total wood = 2 + 4 = 6
    
    6 < 7 (need more wood), H=4 is too high
    Need to lower H: right = mid - 1 = 3

Iteration 2:
    left = 0, right = 3
    mid = (0 + 3) // 2 = 1
    
    Calculate wood cut at height 1:
      - Tree 0: 2 > 1, cut (2 - 1) = 1
      - Tree 1: 6 > 1, cut (6 - 1) = 5
      - Tree 2: 3 > 1, cut (3 - 1) = 2
      - Tree 3: 8 > 1, cut (8 - 1) = 7
      Total wood = 1 + 5 + 2 + 7 = 15
    
    15 >= 7 (enough wood!), H=1 works
    But try to find higher H: result = 1, left = mid + 1 = 2

Iteration 3:
    left = 2, right = 3
    mid = (2 + 3) // 2 = 2
    
    Calculate wood cut at height 2:
      - Tree 0: 2 = 2, no cut (must be strictly greater)
      - Tree 1: 6 > 2, cut (6 - 2) = 4
      - Tree 2: 3 > 2, cut (3 - 2) = 1
      - Tree 3: 8 > 2, cut (8 - 2) = 6
      Total wood = 4 + 1 + 6 = 11
    
    11 >= 7 (enough wood!), H=2 works
    Try to find higher: result = 2, left = mid + 1 = 3

Iteration 4:
    left = 3, right = 3
    mid = (3 + 3) // 2 = 3
    
    Calculate wood cut at height 3:
      - Tree 0: 2 < 3, no cut
      - Tree 1: 6 > 3, cut (6 - 3) = 3
      - Tree 2: 3 = 3, no cut
      - Tree 3: 8 > 3, cut (8 - 3) = 5
      Total wood = 3 + 5 = 8
    
    8 >= 7 (enough wood!), H=3 works
    Try to find higher: result = 3, left = mid + 1 = 4

Iteration 5:
    left = 4, right = 3
    Loop ends (left > right)

FINAL ANSWER: 3 ✓

Verification:
- H=3: wood = 8 ✓ (>= 7)
- H=4: wood = 6 ✗ (< 7)
So 3 is indeed the highest setting that yields at least 7 meters.

"""


def woodcut(heights, k):
    """
    Find the highest cutting height such that at least k meters of wood is cut.
    
    Args:
        heights (list[int]): Array of tree heights
        k (int): Minimum amount of wood needed
    
    Returns:
        int: The highest possible cutting height H
    """
    if not heights:
        return 0
    
    def calculateWood(heights, h):
        """Calculate total wood cut at height h"""
        total = 0
        for height in heights:
            if height > h:
                total += height - h
        return total
    
    left = 0
    right = max(heights)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        wood = calculateWood(heights, mid)
        
        if wood >= k:
            # We got enough wood at this height
            # Try to find a higher height
            result = mid
            left = mid + 1
        else:
            # Not enough wood at this height
            # Need to lower the height
            right = mid - 1
    
    return result


# ========================================
# TEST CASES
# ========================================

def test_woodcut():
    """Test cases for the woodcut function"""
    
    # Test Case 1: Example from problem
    assert woodcut([2, 6, 3, 8], 7) == 3, "Test Case 1 Failed"
    print("✓ Test Case 1 Passed: Example case")
    
    # Test Case 2: Single tree
    assert woodcut([10], 5) == 5, "Test Case 2 Failed"
    print("✓ Test Case 2 Passed: Single tree")
    
    # Test Case 3: All same height
    assert woodcut([5, 5, 5, 5], 6) == 3, "Test Case 3 Failed"
    # At h=3: (5-3)*4 = 8 >= 6 ✓
    # At h=4: (5-4)*4 = 4 < 6 ✗
    print("✓ Test Case 3 Passed: All same height")
    
    # Test Case 4: Large trees
    assert woodcut([100, 50, 80], 50) == 60, "Test Case 4 Failed"
    print("✓ Test Case 4 Passed: Large trees")
    
    # Test Case 5: Many small trees
    assert woodcut([1, 1, 1, 1, 1], 2) == 0, "Test Case 5 Failed"
    # At h=0: (1-0)*5 = 5 >= 2 ✓
    # At h=1: all trees = height, so 0 cut < 2 ✗
    print("✓ Test Case 5 Passed: Many small trees")
    
    # Test Case 6: Two tall trees
    assert woodcut([5, 15], 10) == 5, "Test Case 6 Failed"
    print("✓ Test Case 6 Passed: Two tall trees")
    
    # Test Case 7: Exactly at one height
    assert woodcut([10, 20, 30], 30) == 10, "Test Case 7 Failed"
    # At h=10: (20-10) + (30-10) = 10 + 20 = 30 >= 30 ✓
    # At h=11: (20-11) + (30-11) = 9 + 19 = 28 < 30 ✗
    print("✓ Test Case 7 Passed: Exactly at one height")
    
    # Test Case 8: Minimum requirement
    heights = [2, 6, 3, 8]
    wood_at_3 = (6-3) + (8-3)  # 3 + 5 = 8
    assert woodcut(heights, wood_at_3) == 3, "Test Case 8 Failed"
    print("✓ Test Case 8 Passed: Minimum requirement")
    
    # Test Case 9: Ascending heights
    assert woodcut([1, 2, 3, 4, 5], 5) == 2, "Test Case 9 Failed"
    print("✓ Test Case 9 Passed: Ascending heights")
    
    # Test Case 10: Descending heights
    assert woodcut([10, 8, 6, 4, 2], 15) == 3, "Test Case 10 Failed"
    # At h=3: (10-3) + (8-3) + (6-3) + (4-3) = 7 + 5 + 3 + 1 = 16 >= 15 ✓
    # At h=4: (10-4) + (8-4) + (6-4) = 6 + 4 + 2 = 12 < 15 ✗
    print("✓ Test Case 10 Passed: Descending heights")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    # Run tests
    test_woodcut()
    
    # Example usage
    print("\n" + "="*50)
    print("EXAMPLE USAGE:")
    print("="*50)
    
    heights = [2, 6, 3, 8]
    k = 7
    result = woodcut(heights, k)
    print(f"Input: heights = {heights}, k = {k}")
    print(f"Output: {result}")
    
    # Verify the answer
    wood_cut = sum(max(0, h - result) for h in heights)
    print(f"\nVerification:")
    print(f"  At height {result}:")
    for i, h in enumerate(heights):
        if h > result:
            print(f"    Tree {i} (height {h}): cut {h - result} meters")
        else:
            print(f"    Tree {i} (height {h}): no cut")
    print(f"  Total wood cut: {wood_cut} meters (required: {k} meters)")
    print(f"  Valid: {wood_cut >= k} ✓")
    
    # Test what happens at height+1
    result_plus_1 = result + 1
    wood_cut_plus_1 = sum(max(0, h - result_plus_1) for h in heights)
    print(f"\n  At height {result_plus_1}:")
    print(f"  Total wood cut: {wood_cut_plus_1} meters")
    print(f"  Valid: {wood_cut_plus_1 >= k} (This should be False to confirm {result} is the max)")
