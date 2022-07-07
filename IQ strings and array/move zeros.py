from typing import List
class Solution:
    def moveZeroes(self,nums:List[int]):
        j=0
        n=len(nums)
        for num in nums:
            if num!=0:
                nums[j]=num
                j+=1
        for x in range(j,n):
            nums[x]=0
        return nums
a1=[1,4,5,0,6,0,3,2,9]
s1=Solution()
print(s1.moveZeroes(a1))