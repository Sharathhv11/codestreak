# Two Sum

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Hash Table
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 13.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a hash map (dictionary in Python) to store numbers encountered so far and their indices. For each number, it checks if the complement (target - current number) exists in the hash map. If it does, the indices are returned. Otherwise, the current number and its index are added to the hash map. This allows for a single pass through the array.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
