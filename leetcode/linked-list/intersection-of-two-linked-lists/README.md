# Intersection Of Two Linked Lists

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Linked List
- **Language:** python
- **Runtime:** 260 ms
- **Memory:** 66.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(M + N)
- **Space Complexity:** O(1)

## Explanation
The solution uses a two-pointer approach where both pointers traverse their respective lists. When a pointer reaches the end of its list, it is reset to the head of the other list. This ensures that both pointers travel the same total distance (length of list A + length of list B) before they meet at the intersection node, or both become None if there's no intersection. This clever trick avoids the need for extra space to store lengths or nodes.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
