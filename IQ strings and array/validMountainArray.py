class Solution:
    def validMountainFunction(self,A):
        if len(A)<3:
            return False
        i=1
        while i<len(A) and A[i]>A[i-1]:
            i+=1
        if i==1 or i==len(A):
            return False
        while i<len(A)and A[i]<A[i-1]:
            i+=1
        return True

a1=[1,5,7,4,2,1]
s1=Solution()
print(s1.validMountainFunction(a1))