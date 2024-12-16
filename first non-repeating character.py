'''
Find the first non-repeating character
Return the first non-repeating char in a string.

'''
def first_nonrepeating_char(str):
    repeated = set()
    visited = set()
    for s in str: 
        if s not in visited:
            if s not in repeated:
                visited.add(s)
            
        elif s in visited:
            visited.remove(s)
            repeated.add(s)

    if len(visited) == 0:
        return None 
    for s in str:
        if s in visited:
            return s
        
def first_nonrepeating_char_option2(str):
    char_count = {}
    for s in str:
        char_count[s] = char_count.get(s, 0) + 1

    # Find the first character with a frequency of 1
    for s in str:
        if char_count[s] == 1:
            return s
    
    return None 

print(first_nonrepeating_char("zfgaffdfrozap"))