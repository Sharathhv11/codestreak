# Subset Sums

## Problem Information
- **Platform:** GeeksforGeeks
- **Concept / Pattern:** Backtracking
- **Language:** python3
- **Runtime:** 0.22s
- **Memory:** 1115/1115 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(2^N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a recursive backtracking approach to explore all possible subsets. For each element, it has two choices: either include it in the current subset sum or exclude it. This leads to 2^N possible subsets, hence the time complexity. The space complexity is O(N) due to the recursion depth.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
