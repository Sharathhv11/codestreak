# Remove Nth Node From End Of List

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Linked List
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 12.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(L)
- **Space Complexity:** O(1)

## Explanation
The solution uses the two-pointer technique. A fast pointer advances N nodes ahead of a slow pointer. When the fast pointer reaches the end, the slow pointer will be at the node preceding the one to be removed, allowing for its deletion in O(L) time and O(1) space.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
