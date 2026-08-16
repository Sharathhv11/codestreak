# Missing And Repeating

## Problem Information
- **Platform:** GeeksforGeeks
- **Language:** python3
- **Runtime:** 1.1s
- **Memory:** 1111/1111 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses the array itself to store information about the presence of numbers. It first places each number in its correct index using swaps. During this process, if a number is already in its correct position or if a duplicate is found, it's handled. Finally, it iterates through the modified array to find the missing number based on the elements' positions. This approach avoids extra space and ensures each element is visited at most a constant number of times.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
