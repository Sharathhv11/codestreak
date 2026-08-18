# Reverse Nodes In K Group

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Linked List
- **Language:** python
- **Runtime:** 8 ms
- **Memory:** 14.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution iterates through the linked list, reversing groups of k nodes. It uses a helper function `reverse` to reverse a sublist and carefully manages pointers to connect the reversed groups. The overall time complexity is O(N) as each node is visited and processed a constant number of times, and space complexity is O(1) due to in-place reversal.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
