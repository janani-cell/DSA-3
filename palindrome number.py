class Solution:
    def isPalindrome(self, x):
        s = str(x)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
#we used two pointers technique method-1
