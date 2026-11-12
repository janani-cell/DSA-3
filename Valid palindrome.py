class Solution:
    def isPalindrome(self,s):
        left = 0
        right = len(s)-1
        while left < right:
            while left<right and not s[left].isalnum():
                left +=1
            while left<right and not s[right].isalnum():
                right -=1
            if s[left].lower()!=s[right].lower():
                return False
            left +=1
            right -=1
        return True
# we used two pointers technique for the above following problem.
#method-1 is used which means opposite direction.
#we have taken left=0 right=len(s)-1 which indicates the positions
# while left<right and not s[left].isalnum(): it indicates that  commas, spaces are there 
#left +-1 means skip these commas, spaces
#same for right but right-=1 in reverse direction
#if s[left].lower()!=s[right].lower(): a! = a then return(False)
#if True then left+=1; right-=1 these 2 lines will be executed.
#so finally we get return(True)
#Input:
#s = " "
#Output: true
#here why it is True means left=0; right=0 because it is empty so while left<right --> means 0<0 it is not True so 
# it will not execute inside the block
# at last return(True) will be executed.
           
