# Queue Using Array

## Problem Information
- **Platform:** GeeksforGeeks
- **Concept / Pattern:** Queue
- **Language:** python3
- **Runtime:** 0.03s
- **Memory:** 1120/1120 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** [object Object]
- **Space Complexity:** O(N)

## Explanation
The solution implements a queue using a Python list. Enqueue and checking fullness/emptiness are O(1) due to list append. Dequeue, however, is O(N) because list.remove(list[0]) requires shifting all subsequent elements. Space complexity is O(N) as it stores up to N elements.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
