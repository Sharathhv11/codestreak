# Two Sum

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Hash Table
- **Language:** python
- **Runtime:** 2 ms
- **Memory:** 13.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a hash table (dictionary in Python) to store numbers encountered so far and their indices. For each number, it checks if the 'complement' (target - current number) exists in the hash table. If it does, the indices are returned. This approach allows for O(N) time complexity as dictionary lookups and insertions are O(1) on average. The space complexity is O(N) due to the storage of elements in the hash table.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
