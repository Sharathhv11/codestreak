# Max Consecutive Ones

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Arrays
- **Language:** python
- **Runtime:** 45 ms
- **Memory:** 16.1 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution iterates through the array once, maintaining a count of consecutive ones. When a zero is encountered, the current count is compared with the maximum count found so far, and the count is reset. The maximum count is updated one last time after the loop to account for trailing ones. This approach ensures a single pass over the array, resulting in linear time complexity and constant space complexity as only a few variables are used.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
