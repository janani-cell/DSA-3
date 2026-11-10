class Solution:
    def removeDuplicates(self, nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return(slow+1)
#these is type-2 in two pointers. Which is called same direction. 
#here we use two words slow, fast.they move in same direction.
#many members think that these method only used for sorted but, 
#no these is also used for unsorted array and sorted array for both.
#slow=0 indicates it's position it is not a number it starts at position 1
#here fast indicates that every element in array.
#nums[fast]!=condition means 1!=1 not True so again it goes 2!=1
#it is True when slow+1=1+1=2
#now nums[slow]=nums[fast] 2=2 so
#It return(slow+1)
