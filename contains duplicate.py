class Solution:
    def containsDuplicate(self, nums):
        return len(nums)!=len(set(nums))
        #here nums=[1,2,3,1]
        #4!=3
      #so it returns True , time complexity is O(n) because i am visiting each element and checking
      #my logic is:
a=[1,2,3,1]
for x in a:
  if x!=x:
    print("False")
  else:
    print("True")
    #these is my logic is
    
