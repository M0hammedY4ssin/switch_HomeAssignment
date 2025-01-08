'''
How would you make this work?
add(2, 5); // 7
add(2)(5); // 7 
'''

def add(x, y = None):
    if  y:
        return x + y
    def inner_add(y):
        return x + y
    return inner_add





print(add(2, 5))
print(add(2)(5))