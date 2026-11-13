class Solution:
    def reverseString(self,s):
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return(s)
#we used two pointers methos-1 technique.
#s[left],s[right] = s[right],s[left] these is the main condition we used here.
