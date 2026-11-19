class Solution:
    def validMountainArray(self,arr):
        n=len(arr)
        if n<3:
            return False
        left=0
        right=n-1
        while left<n-1 and arr[left]<arr[left+1]:
            left+=1
        while right>0 and arr[right]<arr[right-1]:
            right-=1
        return left==right and left!=0 and right!=n-1
#here we used two pinters technique method-1. 
#valid mountain array means like [1,2,3,2,1] ; [0,4,5,6,5,4,2] these all are examples of valid mountain array.
#time complexity is O(n) we know it is common for two pointers.
#actually before stepping into these actual code my actual thing code was, my logic was:
a=[1,2,3,2,1]
if a[0]==a[4] and a[1]==a[3]:
    print("True")
else:
    print("False")
#these was my logic only and its time complexity is O(1) because i had not used any loop here.
