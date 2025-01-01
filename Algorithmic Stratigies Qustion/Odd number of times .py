''' 
Odd number of times  

Given an array, find the int that appears an odd number of times.
'''

def odd_number_of_time(nums):
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1
    
    for num in nums:
        if num_count[num] % 2 == 1:
            return num
    

    return None

print(odd_number_of_time([1,2,3,33,2,1,2,4,3,5]))