a=[1,2,3,3,4,4,2]
if 2!=22 or 3!=33 or 4!=44:
  print("1")
else:
  print("none")
  #here question is you should print any one element from here not more than one element of particular ones.
  #here i wrote my logic how i thaught first myself , how i tried ,
  #time complexity for my code is O(1) because it is just printing don't even have loop.
  def singleNumber(self, nums):
        for num in nums:
            if nums.count(num)==1:
                return num
#these is the real code in which we used count method , time complexity is O(n²)
#because we used count inside a loop where it checks many times, for counting whenever it is used inside a loop always O(n²).
