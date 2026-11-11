class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            need=target-num
            if need in seen:
                return[seen[need],i]
            seen[num]=i
        return[]
#here we used a method called hashmap which plays a crucial role in Data Structures. First, 
#you have to remember the three main lines of these hashmap,First one is-
#take empty dictionary like use a variable seen={}
#the main core formula of hashmap is need = target - num
#the third is return[seen[need],i]-- it indicates that return the old position and new position.
#the fourth is seen[num]=i-- indicates that if not found store in me
