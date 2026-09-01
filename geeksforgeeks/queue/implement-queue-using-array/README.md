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
The solution implements a queue using a Python list. While `enqueue`, `getFront`, `getRear`, `isEmpty`, and `isFull` are O(1), `dequeue` is O(N) because `list.remove(list[0])` requires shifting all subsequent elements. The space complexity is O(N) to store up to 'n' elements.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
