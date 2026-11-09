class Solution:
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
           s=numbers[left]+numbers[right]
           if s == target:
              return(left+1, right+1)
           elif s < target:
               left+=1
           else:
                right-=1

    #here we used concept of Two Pointer of method-I opposite direction.
     It should be used when array is sorted. These Two Pointer technique is used when
     array is sorted...    
