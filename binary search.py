def binary(arr, n):
	right = len(arr)
	left = 0
	while right >= left: 
        mid = (left+right)//2 
        if arr[mid] == n:
            return mid
        elif arr[mid] < n :
            right= mid 
        elif arr[mid] > n:
            left = mid
		
    return -1

# binary([1, 2, 3, 4, 5], 1), 0)	
# ----------------------------------------------------------------------------------------------------
def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        
        # left = arr[:mid]
        # right = arr[mid:]
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)



def merge(arr, left,mid, right):
    left_length = mid - left +1
    right_length = right - mid

    temp_left = [0] * left_length
    temp_right = [0] * right_length

    for i in range(left_length):
       temp_left[i]= arr[left + i]
    for j in range(right_length):
        temp_right[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray
   
    while i < left_length and j < right_length:
        if temp_left[i] <= temp_right[j]:
           arr[k]= temp_left[i]
           i +=1
        else:
           arr[k]= temp_right[j]
           j += 1
        
        k+=1
       
    while i < left_length: 
        arr[k]= temp_left[i]
        i +=1
        k+=1

    while j < right_length:
        arr[k]= temp_right[j]
        j += 1
        k += 1
    return 

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr)-1)
print("merge sort: ", arr)

# --------------------------------------------------------------------------------------

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot= arr[high]
    i = low -1

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)
print("qucick sort: ", arr)