'''
Largest of 3
Write a function that receives 3 numbers and return the biggest one.
You are not allowed to use any functions including built in ones.

'''
def largest_of3(a, b, c):
    max = largest_of2(a, b)
    return largest_of2(max, c)

def largest_of2(a, b):
    if a > b:
        return a
    else: return b