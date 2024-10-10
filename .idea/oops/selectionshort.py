def sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
nums=[2,46,32,6,3,7,33,8,3,7,3,8,3,8]
sort(nums)
print(nums)
