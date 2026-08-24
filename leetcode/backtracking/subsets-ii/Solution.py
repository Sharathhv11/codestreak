class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [] 
     
        def backtracking(i,subset):
            if( i == len(nums) ):
                res.append(list(subset))
                return

            subset.append(nums[i])
            backtracking(i+1,subset)

            
            subset.pop()

            if( len(subset) > 0 and subset[-1] == nums[i] ):
                return
            backtracking(i+1,subset)
        
        backtracking(0,[])
        return res
        