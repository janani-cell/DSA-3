class Solution:
    def getConcatenation(self, nums):
        return nums+nums
#here my question is a=[1,2,3]
a=[1,2,3]
print(a+a) these is concatination ,
#i can also write in form of repition operator
print(a*2)
if i want 3 times print(a+a+a)
or print(a*3)
#first i thought time complexity is O(1) because there is only 1 line but wrong 
#it is O(n) because array size increases so it has do some work in it so O(n) means it is doing some operation inside it it has to copy every element so O(n).
