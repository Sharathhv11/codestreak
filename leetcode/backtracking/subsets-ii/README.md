# Subsets Ii

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Backtracking
- **Language:** python
- **Runtime:** 1 ms
- **Memory:** 12.7 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N * 2^N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a backtracking approach to generate all subsets. It sorts the input array to handle duplicates efficiently. At each step, it decides whether to include the current element or not, and skips duplicate elements to avoid redundant subsets, resulting in O(N * 2^N) time complexity and O(N) space complexity for the recursion stack and subset storage.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
