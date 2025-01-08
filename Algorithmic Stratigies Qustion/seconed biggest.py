'''
Second biggest
find the second biggest element in an array

'''
# 0,1,2,3,4 --> 3
# 1 --> 1
# 
def secondbiggest(nums):
    if not nums: 
        return None
    max1, max2 = nums[0], nums[0]

    for num in nums:
        if num > max1:
            max2= max1
            max1 = num 
        
    return max2


# Time O(n)
# Space O(1)

print(secondbiggest([0,1,2,3,4,5]))
print(secondbiggest([]))
print(secondbiggest([1]))