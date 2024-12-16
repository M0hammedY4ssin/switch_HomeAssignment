''' 
Common elements 
Find the common elements between 2 arrays.
1.	Write the brute force solution
2.	Write a solution in O(n)

Common elements in 3 arrays
Find the common elements between 
3 arrays.

'''
def common_elements_2arrays(arr1, arr2):
    my_set =set(arr1)
    common = []
    for n in arr2:
        if n in my_set:
            common.append(n)
            my_set.remove(n)
    
    return common 


def common_elements_3arrays(arr1,arr2,arr3):
    arr = common_elements_2arrays(arr1, arr2)
    common = common_elements_2arrays(arr, arr3)
    return common 