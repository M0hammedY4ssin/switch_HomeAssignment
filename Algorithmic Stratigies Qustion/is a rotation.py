'''
is one word a rotation of the other?
'''
def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    s1= str1 + str1

    index = s1.find(str2)
    if index == -1:
        return False
    return True
# time complexity : o(n)
# space complexity : o(n)


# -----------------------------------

def is_rotation2(str1, str2):
    if len(str1) != len(str2):
        return False
    n = len(str1)
    for i in range(n):
        count=0
        for j in range(n):
            if str1[(i+j)%n]== str2[j]:
                count +=1
        if count == n:
            return True
    
    return False

print(is_rotation2("abccd", "cdabc"))