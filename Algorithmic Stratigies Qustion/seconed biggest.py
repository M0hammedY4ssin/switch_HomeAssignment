'''
Second biggest
find the second biggest element in an array

'''
# 0,1,2,3,4 --> 3
# 1 --> 1
# 
def secondbiggest(array):
    if not array: 
        return None
    max1, max2 = array[0], array[0]

    for n in array:
        if n > max1:
            max2= max1
            max1 = n 
        
    return max2


# Time O(n)
# Space O(1)

print(secondbiggest([0,1,2,3,4,5]))
print(secondbiggest([]))
print(secondbiggest([1]))