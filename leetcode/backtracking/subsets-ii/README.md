# Subsets Ii

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Backtracking
- **Language:** python
- **Runtime:** 1 ms
- **Memory:** 12.7 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(2^N * N)
- **Space Complexity:** O(2^N * N)

## Explanation
The solution uses backtracking to explore all possible subsets. Sorting the input array first allows for efficient duplicate handling by skipping branches that would generate redundant subsets. The time complexity is O(2^N * N) because there are 2^N subsets, and creating each subset can take O(N) time. The space complexity is also O(2^N * N) to store all generated subsets.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
