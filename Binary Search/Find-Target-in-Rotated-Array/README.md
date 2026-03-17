# Find the Target in a Rotated Sorted Array

## Problem Statement

A rotated sorted array is an array of numbers sorted in ascending order, in which a portion of the array is moved from the beginning to the end. For example, a possible rotation of `[1, 2, 3, 4, 5]` is `[3, 4, 5, 1, 2]`, where the first two numbers are moved to the end.

Given a rotated sorted array of **unique numbers**, return the index of a target value. If the target value is not present, return -1.

### Example

```
Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
Output: 2
```

## Key Insight

Even though the array is rotated, **exactly one half is always sorted**. We can use this property to efficiently search using binary search.

## Algorithm

1. **Initialize pointers**: `left = 0`, `right = len(nums) - 1`
2. **Binary search loop**: While `left <= right`:
   - Calculate `mid = (left + right) // 2`
   - If `nums[mid] == target`: return `mid`
   - **Identify sorted half**:
     - If `nums[left] <= nums[mid]`: Left half is sorted
       - If target is in `[nums[left], nums[mid])`: search left
       - Otherwise: search right
     - Otherwise: Right half is sorted
       - If target is in `(nums[mid], nums[right]]`: search right
       - Otherwise: search left
3. **Target not found**: return -1

## Complexity Analysis

| Metric    | Complexity |
| --------- | ---------- |
| **Time**  | O(log n)   |
| **Space** | O(1)       |

### Why O(log n)?

- We use binary search which eliminates half the elements each iteration
- The number of iterations is proportional to log₂(n)

## Visual Example

```
Array: [8, 9, 1, 2, 3, 4, 5, 6, 7]
Target: 1
       0  1  2  3  4  5  6  7  8  (indices)

Step 1: left=0, right=8, mid=4
        nums[mid]=3
        Left half [8,9] is NOT sorted (9 > 3)
        Right half [3,4,5,6,7] IS sorted
        Target 1 NOT in right half [3,7]
        → Search left

Step 2: left=0, right=3, mid=1
        nums[mid]=9
        Left half [8,9] IS sorted
        Target 1 NOT in left half [8,9]
        → Search right

Step 3: left=2, right=3, mid=2
        nums[mid]=1
        Found! Return 2
```

## Edge Cases

1. **Single element**: `[1]`, target=1 → return 0
2. **No rotation** (already sorted): Works like normal binary search
3. **Target not found**: return -1
4. **Rotation at boundary**: Works correctly due to sorted half check

## Implementation Notes

- Works only with **unique** numbers (as per problem statement)
- The rotation point is automatically handled by checking which half is sorted
- No need to explicitly find the rotation point
