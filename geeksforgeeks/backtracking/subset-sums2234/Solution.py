class Solution:
	def subsetSums(self, arr):
		# code here
		result = []
		def backtrack(sum,index):
    	    if( index >= len(arr) ):
    	        result.append(sum)
    	        return
	        
	        backtrack(sum,index+1)
	        backtrack(sum+arr[index],index+1)
	    
		backtrack(0,0)
		return result 