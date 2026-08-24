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
The solution uses backtracking to generate all possible subsets. Sorting the input array first allows for efficient skipping of duplicate subsets by checking the last element added before a recursive call to include the current element. The time complexity is dominated by generating 2^N subsets, and for each subset, copying it takes O(N) time. Space complexity is O(N) for the recursion depth and the subset storage.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
