# Cutting Wood

## Problem Statement

You are given an array representing the heights of trees, and an integer `k` representing the total length of wood that needs to be cut.

A woodcutting machine is set to a certain height `H`. The machine cuts off the top part of all trees taller than `H`, while trees shorter than `H` remain untouched.

**Determine the highest possible setting of the woodcutter (`H`) so that it cuts at least `k` meters of wood.**

Assume the woodcutter cannot be set higher than the height of the tallest tree in the array.

### Example

```
Input: heights = [2, 6, 3, 8], k = 7
Output: 3

Explanation:
  At height 3:
    - Tree at height 2: 2 < 3, no cut
    - Tree at height 6: 6 > 3, cut (6 - 3) = 3 meters
    - Tree at height 3: 3 = 3, no cut
    - Tree at height 8: 8 > 3, cut (8 - 3) = 5 meters

  Total: 3 + 5 = 8 meters ✓ (≥ 7)

  At height 4: (6-4) + (8-4) = 2 + 4 = 6 meters ✗ (< 7)

  Therefore, 3 is the highest setting that yields at least 7 meters.
```

---

## Approach

This is a **Binary Search on the Answer** problem.

### Key Insight

**Monotonic Property**: As the cutting height `H` increases, the total amount of wood cut decreases. This monotonic relationship allows us to use binary search.

### Search Space

- **Lower bound**: 0 (cut everything)
- **Upper bound**: max(heights) (cut nothing)

### Binary Search Strategy

1. Search for the **HIGHEST** height `H` where `total_wood_cut ≥ k`
2. Use left and right pointers to narrow the search range
3. For each middle height, calculate total wood cut
4. **If wood ≥ k**: This height works, try going higher (left = mid + 1)
5. **If wood < k**: Height is too high, go lower (right = mid - 1)

### Why Binary Search?

| Approach                         | Time Complexity           | Why Better                 |
| -------------------------------- | ------------------------- | -------------------------- |
| Brute Force (check every height) | O(n × max_height)         | Too slow for large heights |
| **Binary Search**                | **O(n × log max_height)** | **Much more efficient!**   |

**Example**: For 1000 trees with max height 10,000:

- Brute force: 1,000 × 10,000 = **10,000,000** operations
- Binary search: 1,000 × log(10,000) ≈ 1,000 × 14 = **14,000** operations

---

## Complexity Analysis

### Time Complexity: **O(n × log M)**

Where:

- `n` = number of trees (length of heights array)
- `M` = maximum height in the array

**Breakdown**:

- Binary search iterations: O(log M)
- For each iteration, calculate wood cut by checking all trees: O(n)
- Total: O(n × log M)

**Example**: 1000 trees, max height 1000:

- log(1000) ≈ 10 iterations
- 1000 × 10 = **10,000 operations**

### Space Complexity: **O(1)**

- Only constant extra space is used for variables:
  - `left`, `right`, `mid` pointers
  - `result` variable
- No additional data structures that scale with input size
- Space usage is completely independent of input size

---

## Dry Run / Step-by-Step Walkthrough

### Input:

```
heights = [2, 6, 3, 8]
k = 7
```

### Binary Search Process:

```
Initialize:
  left = 0
  right = max(heights) = 8
  result = 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 1:
  left = 0, right = 8
  mid = (0 + 8) // 2 = 4

  Wood cut at height 4:
    Tree 0: 2 < 4 → 0 meters
    Tree 1: 6 > 4 → (6 - 4) = 2 meters
    Tree 2: 3 < 4 → 0 meters
    Tree 3: 8 > 4 → (8 - 4) = 4 meters
    Total: 2 + 4 = 6 meters

  6 < 7 (NOT enough) → Height is too high
  right = mid - 1 = 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 2:
  left = 0, right = 3
  mid = (0 + 3) // 2 = 1

  Wood cut at height 1:
    Tree 0: 2 > 1 → (2 - 1) = 1 meter
    Tree 1: 6 > 1 → (6 - 1) = 5 meters
    Tree 2: 3 > 1 → (3 - 1) = 2 meters
    Tree 3: 8 > 1 → (8 - 1) = 7 meters
    Total: 1 + 5 + 2 + 7 = 15 meters

  15 ≥ 7 (ENOUGH!) → Height works, try higher
  result = 1
  left = mid + 1 = 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 3:
  left = 2, right = 3
  mid = (2 + 3) // 2 = 2

  Wood cut at height 2:
    Tree 0: 2 = 2 → 0 meters (must be strictly higher)
    Tree 1: 6 > 2 → (6 - 2) = 4 meters
    Tree 2: 3 > 2 → (3 - 2) = 1 meter
    Tree 3: 8 > 2 → (8 - 2) = 6 meters
    Total: 4 + 1 + 6 = 11 meters

  11 ≥ 7 (ENOUGH!) → Height works, try higher
  result = 2
  left = mid + 1 = 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 4:
  left = 3, right = 3
  mid = (3 + 3) // 2 = 3

  Wood cut at height 3:
    Tree 0: 2 < 3 → 0 meters
    Tree 1: 6 > 3 → (6 - 3) = 3 meters
    Tree 2: 3 = 3 → 0 meters
    Tree 3: 8 > 3 → (8 - 3) = 5 meters
    Total: 3 + 5 = 8 meters

  8 ≥ 7 (ENOUGH!) → Height works, try higher
  result = 3
  left = mid + 1 = 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteration 5:
  left = 4, right = 3
  Loop exits (left > right)

FINAL ANSWER: 3 ✅
```

### Verification:

- **At height 3**: 8 meters ✓ (≥ 7) → Valid ✓
- **At height 4**: 6 meters ✗ (< 7) → Invalid ✗
- **Therefore**: 3 is the highest valid cutting height

---

## Code Implementation

```python
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
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your system

### Running the Script

1. Navigate to the Cutting-Wood folder:

   ```bash
   cd "c:\self\bytebytego-coding-patterns\Binary Search\Cutting-Wood"
   ```

2. Run the Python file:

   ```bash
   python cutting_wood.py
   ```

3. The script will execute all test cases and display results:
   ```
   ✓ Test Case 1 Passed: Example case
   ✓ Test Case 2 Passed: Single tree
   ...
   ✅ All test cases passed!
   ```

---

## Test Cases

The solution includes **10 comprehensive test cases**:

| Test # | Scenario              | Input                      | Expected Output |
| ------ | --------------------- | -------------------------- | --------------- |
| 1      | Example from problem  | heights=[2,6,3,8], k=7     | 3               |
| 2      | Single tree           | heights=[10], k=5          | 5               |
| 3      | All same height       | heights=[5,5,5,5], k=6     | 3               |
| 4      | Large trees           | heights=[100,50,80], k=50  | 60              |
| 5      | Many small trees      | heights=[1,1,1,1,1], k=2   | 0               |
| 6      | Two tall trees        | heights=[5,15], k=10       | 5               |
| 7      | Exactly at one height | heights=[10,20,30], k=30   | 10              |
| 8      | Minimum requirement   | heights=[2,6,3,8], k=8     | 3               |
| 9      | Ascending heights     | heights=[1,2,3,4,5], k=5   | 2               |
| 10     | Descending heights    | heights=[10,8,6,4,2], k=15 | 3               |

---

## Key Insights

1. **Monotonic Decrease**: As cutting height increases, wood amount decreases linearly. This property is crucial for binary search validity.

2. **Binary Search on Answer**: Instead of searching for a specific element, we search for the maximum value that satisfies a condition (wood ≥ k).

3. **Efficiency Gain**: Without binary search, we'd check every possible height from 0 to max(heights). Binary search reduces iterations from O(max_height) to O(log max_height).

4. **Edge Cases Handled**:
   - Empty array
   - Single tree
   - All trees same height
   - Very tall/short trees
   - Ascending/descending height arrays

5. **Correctness Guarantee**: The algorithm finds the HIGHEST valid height because:
   - When `wood ≥ k`, we update `result = mid` and search higher
   - When `wood < k`, we search lower
   - We continue until `left > right`, ensuring we've found the maximum

---

## Visual Representation

```
Height vs Wood Cut (for heights = [2, 6, 3, 8], k = 7)

Wood Cut (meters)
      |
   30 |●                    (h=0)
      |
   25 |
      |    ●
   20 |              (h=1)
      |
   15 |
      |        ●     ← Target zone (≥ 7)
   10 |           (h=2)
      |
    8 |         ●   ← Result: h=3, wood=8 ✓
      |
    6 |           ●        (h=4)  Too high!
      |
    4 |             ●     (h=5)
      |
    2 |               ●   (h=6)
      |
    0 |________________●___ (h=8) - max height
      0   1   2   3   4   5   6   7   8
                  Height (H)

As height increases → wood decreases (monotonic)
We find the rightmost point in the valid zone (≥ 7)
```

---

## Real-World Application

This problem models real-world scenarios:

- **Lumber Production**: Setting a machine to optimal height to meet production targets while maximizing efficiency
- **Resource Management**: Finding the optimal threshold to meet minimum requirements
- **Quality Control**: Balancing output quantity (k meters) with machine settings (height)

---

## References

- **Pattern**: Binary Search on the Answer
- **Difficulty**: Medium
- **Source**: ByteByteGo Coding Patterns
- **Link**: https://bytebytego.com/exercises/coding-patterns/binary-search/cutting-wood
- **Related Concepts**: Monotonic Functions, Binary Search Variations
