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
The solution implements a queue using a Python list. While most operations like initialization, isEmpty, isFull, getFront, and getRear are O(1), the dequeue operation is inefficient. `list.remove(list[0])` takes O(N) time because it requires shifting all subsequent elements to fill the gap left by the removed first element.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
