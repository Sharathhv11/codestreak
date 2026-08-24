# Remove Duplicates From Sorted Array

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Two Pointers
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 13.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses the two-pointer technique. One pointer 'k' tracks the position of the last unique element found, while the other pointer 'i' iterates through the array. If a new unique element is encountered at 'i', it's swapped to the position after 'k', and 'k' is incremented. This modifies the array in-place, resulting in O(1) space complexity, and processes each element once, yielding O(N) time complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
