# Two Sum

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Hash Table
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 13.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a hash table (dictionary in Python) to store numbers encountered so far and their indices. For each number, it calculates the complement needed to reach the target and checks if the complement exists in the hash table. If found, it returns the indices; otherwise, it adds the current number and its index to the hash table. This allows for O(N) time complexity due to constant-time average lookups and insertions in the hash table, but requires O(N) space for the hash table.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
