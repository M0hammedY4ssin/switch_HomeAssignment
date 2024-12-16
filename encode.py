'''
Chars to Lengths   
We want to count for each letter how many times it repeats one after the other. 
For a string aaabbcb, it will print output a3b2c1b1

'''
def encode(word):
    counter = 0 
    encoded_string = ""
    index = 0
    while index < len(word):
        c = word[index]
        while index < len(word) and c == word[index]:
            counter +=1
            index +=1
        encoded_string += c + str(counter) 
        counter = 0
    
    return encoded_string

print(encode("aaabefeeff"))