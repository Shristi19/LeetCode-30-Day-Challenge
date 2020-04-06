def remove_zeros(nums):
    for i in range(0,len(nums)):
        if nums[i] ==0:
            nums.remove(nums[i])
            nums.append(0)
    print(nums)

remove_zeros([1,3,0,23,45,0,6,7,8,0])
