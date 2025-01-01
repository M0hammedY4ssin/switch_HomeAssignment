'''
Trapping Rainwater Problem states that given an array of n non-negative integers arr[] 
representing an elevation map where the width of each bar is 1,
compute how much water it can trap after rain. 

Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Tasks:
1.	Write a brute force solution
2.	Write an efficient solution in O(n)
3.	Solve the problem but now return the max amount of water that can be trapped between 2 buildings

'''
#------------Task 2------------
def trapping_water(arr):

    l,r=0, len(arr)-1
    leftmax, rightmax = arr[l],arr[r]
    res = 0
    while l < r:
        if leftmax< rightmax:
            l+=1
            leftmax= max(leftmax,arr[l])
            res += leftmax - arr[l]
        else:
            r-=1
            rightmax= max(rightmax,arr[r])
            res += rightmax - arr[r]
    return res

# Time O(n)
# Space O(n)
print(trapping_water([3, 0, 1, 0, 4, 0, 2])) # output = 10

#------------Task 3------------
def max_trapping_water(arr):
    l,r=0, len(arr)-1
    max_area=0
    while l < r  :
        area = min(arr[l],arr[r]) * (r-l)
        max_area= max(max_area, area)
        if arr[r] > arr[l]:
            l+=1
        else:
            r-=1
    return max_area 

# Time O(n)
# Space O(1)

# print(max_trapping_water([1,7,2,5,4,7,3,6])) # output = 36
# print(max_trapping_water([2,2,2])) # output = 4
# print(max_trapping_water([3, 0, 1, 0, 4, 0, 2])) # output = 12