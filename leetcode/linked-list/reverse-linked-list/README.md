# Reverse Linked List

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Linked List
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 14.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution iteratively traverses the linked list, reversing the 'next' pointer of each node to point to the previous node. This is achieved using three pointers: 'previous', 'current' (p), and 'next_node' (next), to keep track of the nodes during the reversal. The time complexity is O(N) because each node is visited once, and the space complexity is O(1) as only a constant amount of extra space is used for the pointers.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
