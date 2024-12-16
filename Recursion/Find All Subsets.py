'''
Find All Subsets of a Set
-	Problem: Write a recursive function find_subsets(lst) that returns all possible subsets of a given list of unique elements.
-	Example: find_subsets([1, 2]) should return [[], [1], [2], [1, 2]].

'''
def find_subsets(myset):
    if not myset:
        return {}
    element = myset.pop()
    my_subsets = find_subsets(myset)
    
    return my_subsets 