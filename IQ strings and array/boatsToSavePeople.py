class Solution:
    def numResucueBoats(self,people:list[int],limit:int):
        people.sort()
        left=0
        right=len(people)-1
        boat_number=0
        while(left<=right):
            if(left==right):
                boat_number+=1
            elif(people[left]+people[right]<=limit):
                left+=1
                right-=1
                boat_number+=1
            else:
                right-=1
                boat_number+=1
        return boat_number 
a1=[2,3,4,5,1]
s1=Solution()
print(s1.numResucueBoats(a1,5))       