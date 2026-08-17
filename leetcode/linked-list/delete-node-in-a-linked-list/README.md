# Delete Node In A Linked List

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Linked List
- **Language:** python
- **Runtime:** 14 ms
- **Memory:** 12.7 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution works by copying the value of the next node into the current node and then deleting the next node. This effectively removes the current node by overwriting its value and then bypassing it in the list. The time complexity is O(N) because in the worst case, we might have to traverse almost the entire list to find a node to copy from. The space complexity is O(1) as we are only using a few extra variables.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
