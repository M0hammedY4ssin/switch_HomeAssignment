'''
Closest Number

Find in a sorted array the closest number to a given number
'''

def closest_number(n, nums):
    closest = nums[0]
    for num in nums:
        # if abs(n - num) == abs(n - closest):
        #     closest = min(closest , num)
        # elif abs(n - num) < abs(n - closest):
        #     closest = num

        if abs(n - num) < abs(n - closest) or (abs(n - num) == abs(n - closest) and num < closest):
            closest = num

    return closest


print(closest_number(9, [1,7,10,9,8]))
print(closest_number(9, [1,7,10,8,6]))