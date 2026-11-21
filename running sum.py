#here question is a=[1,2,3,4]
#I want output as a=[1,3,6,10]
#these is my logic how i built?
a=[1,2,3,4]
print(a[0],end=" ")
print(a[0] + a[1], end=" ")
print(a[0] + a[1] + a[2], end=" ")
print(a[0] + a[1] + a[2] + a[3], end=" ")
#but these is applicable for only specific numbers not upto 100 numbers so thats why we use leetcode pattern,  
#for my logic time complexity is O(n) because i am visiting each element and performing operation.
class Solution:
    def runningSum(self, nums):
        result=[]
        total=0
        for x in nums:
            total+=x
            result.append(total)
        return result
#time complexity is O(n) because there is one loop and visiting each element in array and performing operation.      
