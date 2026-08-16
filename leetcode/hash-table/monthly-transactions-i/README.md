# Monthly Transactions I

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Hash Table
- **Language:** mysql
- **Runtime:** 608 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The query first calculates the total transactions per month and country, and then it performs a left join with a subquery that calculates approved transactions per month and country. The subquery also takes O(N) time. The overall time and space complexity are O(N) due to processing the entire transaction table twice and storing intermediate results.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
