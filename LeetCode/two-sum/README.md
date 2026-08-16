# Two Sum

## Problem Information
- **Platform:** LeetCode
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 13.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a hash map (dictionary) to store numbers encountered so far and their indices. For each number, it checks if the complement (target - current_number) exists in the hash map. If it does, the indices are returned. Otherwise, the current number and its index are added to the hash map. This approach iterates through the list once, leading to O(N) time complexity, and the hash map can store up to N elements, resulting in O(N) space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
