def find_max(nums):
    biggest = nums[0]
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest
print(find_max([3, 10, 5, 20, 8]))  
#time complexity is O(n) because we have only one loop.
#here my logic is
a=[1,2,3,4,3,2,4]
print(max(a))
#time complexity is O(n) because we are travelling each time.

