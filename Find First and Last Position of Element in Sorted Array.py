#First guess: binary search and shift the index to left and right bound
#time complexity O(logn)
#however,
#intuitive method is linear search : O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        #base case test
        if(nums == None or len(nums) ==0):
            return [-1,-1]
        if(len(nums)==1):
            if(nums[0] == target):
                return [0,0]
            else:
                return [-1,-1]
        while(r>=l):
            mid = int(l + (r-l)/2)
            if(nums[mid] == target):
                l = mid
                r = mid
                while(l>0 and nums[l-1] == nums[l]):
                    l-=1
                while(r < len(nums)-1 and nums[r+1] == nums[r]):
                    r+=1
                return [l,r]
            elif(nums[mid] < target):
                l = mid + 1
            elif(nums[mid] > target):
                r = mid - 1
        return[-1,-1]     
            
        
        