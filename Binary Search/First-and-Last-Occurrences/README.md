# First and Last Occurrences of a Number

## Problem Statement

Given an array of integers sorted in non-decreasing order, return the first and last indexes of a target number. If the target is not found, return `[-1, -1]`.

### Example

```
Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
Output: [3, 5]

Explanation: The first and last occurrences of number 4 are at indexes 3 and 5.
```

---

## Approach

This solution uses the **Binary Search** technique with two modified binary search operations:

### 1. **Find First Occurrence (Leftmost Position)**

- Perform binary search looking for the target
- When found, continue searching **left** to find the leftmost occurrence
- Move the right pointer to `mid - 1` when target is found

### 2. **Find Last Occurrence (Rightmost Position)**

- Perform binary search looking for the target
- When found, continue searching **right** to find the rightmost occurrence
- Move the left pointer to `mid + 1` when target is found

### Why Binary Search?

Since the array is **sorted**, we can eliminate half of the remaining elements in each iteration, making it highly efficient.

---

## Complexity Analysis

### Time Complexity: **O(log n)**

- We perform **two binary searches** (for first and last occurrences)
- Each binary search takes O(log n) time
- Total: O(log n) + O(log n) = **O(log n)**

**Why O(log n)?** Because the search space is halved in each iteration:

- Iteration 1: n elements
- Iteration 2: n/2 elements
- Iteration 3: n/4 elements
- ... and so on until we reach 1 element

### Space Complexity: **O(1)**

- Only a constant amount of extra space is used
- Variables: `left`, `right`, `mid`, `result`
- No additional data structures that scale with input size
- Space usage is independent of the input size

---

## Dry Run / Step-by-Step Walkthrough

### Input:

```
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
target = 4
indices: 0  1  2  3  4  5  6  7  8  9  10 11 12
```

### Finding First Occurrence:

```
Iteration 1:
  left = 0, right = 12
  mid = (0 + 12) // 2 = 6
  nums[6] = 5 > 4 → move right: right = 5

Iteration 2:
  left = 0, right = 5
  mid = (0 + 5) // 2 = 2
  nums[2] = 3 < 4 → move left: left = 3

Iteration 3:
  left = 3, right = 5
  mid = (3 + 5) // 2 = 4
  nums[4] = 4 ✓ FOUND, continue left: right = 3

Iteration 4:
  left = 3, right = 3
  mid = 3
  nums[3] = 4 ✓ FOUND, continue left: right = 2

Iteration 5:
  left = 3, right = 2
  Loop ends (left > right)

Result: First = 3 ✓
```

### Finding Last Occurrence:

```
Iteration 1:
  left = 0, right = 12
  mid = 6
  nums[6] = 5 > 4 → right = 5

Iteration 2:
  left = 0, right = 5
  mid = 2
  nums[2] = 3 < 4 → left = 3

Iteration 3:
  left = 3, right = 5
  mid = 4
  nums[4] = 4 ✓ FOUND, continue right: left = 5

Iteration 4:
  left = 5, right = 5
  mid = 5
  nums[5] = 4 ✓ FOUND, continue right: left = 6

Iteration 5:
  left = 6, right = 5
  Loop ends (left > right)

Result: Last = 5 ✓
```

### Final Answer: `[3, 5]` ✅

---

## Code Implementation

```python
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

    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first = findFirst(nums, target)

    if first == -1:
        return [-1, -1]

    last = findLast(nums, target)
    return [first, last]
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your system

### Running the Script

1. Navigate to the First-and-Last-Occurrences folder:

   ```bash
   cd "c:\self\bytebytego-coding-patterns\Binary Search\First-and-Last-Occurrences"
   ```

2. Run the Python file:

   ```bash
   python first_and_last_occurrences.py
   ```

3. The script will execute all test cases and display results:
   ```
   ✓ Test Case 1 Passed: Multiple occurrences
   ✓ Test Case 2 Passed: Single occurrence
   ✓ Test Case 3 Passed: Target not found
   ...
   ✅ All test cases passed!
   ```

---

## Test Cases

The solution includes **10 comprehensive test cases**:

| Test # | Scenario                   | Input                                        | Expected Output |
| ------ | -------------------------- | -------------------------------------------- | --------------- |
| 1      | Multiple occurrences       | nums=[1,2,3,4,4,4,5,6,7,8,9,10,11], target=4 | [3, 5]          |
| 2      | Single occurrence          | nums=[1,2,3,4,5,6,7], target=5               | [4, 4]          |
| 3      | Target not found           | nums=[1,2,3,5,6,7], target=4                 | [-1, -1]        |
| 4      | Target at beginning        | nums=[4,4,4,5,6,7], target=4                 | [0, 2]          |
| 5      | Target at end              | nums=[1,2,3,4,4,4], target=4                 | [3, 5]          |
| 6      | Empty array                | nums=[], target=4                            | [-1, -1]        |
| 7      | Single element (found)     | nums=[5], target=5                           | [0, 0]          |
| 8      | Single element (not found) | nums=[5], target=3                           | [-1, -1]        |
| 9      | All elements are target    | nums=[4,4,4,4,4], target=4                   | [0, 4]          |
| 10     | Large array                | Large array with duplicates                  | [99, 149]       |

---

## Key Insights

1. **Two Separate Searches**: We don't use a single binary search to find both positions because one search can't efficiently find both at once.

2. **Continue Searching When Found**: The key difference from standard binary search is that when we find the target, we continue searching in one direction (left for first, right for last) instead of stopping immediately.

3. **Efficiency**: By using binary search twice instead of linear traversal, we achieve O(log n) instead of O(n).

4. **Edge Cases Handled**:
   - Empty array
   - Single element array
   - Target not found
   - Target at boundaries
   - Multiple consecutive duplicates

---

## References

- **Pattern**: Binary Search with Modification
- **Difficulty**: Medium
- **Source**: ByteByteGo Coding Patterns
- **Link**: https://bytebytego.com/exercises/coding-patterns/binary-search/first-and-last-occurrences-of-a-number
