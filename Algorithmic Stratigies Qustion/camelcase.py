'''
Camelcase

Write a simple camelCase method for strings. All words (except for the first) must have their first letter capitalized without spaces.
'''
def to_camelcase(sentence):
    cameled = ""
    words = sentence.split(" ")
    cameled = words[0].tolower() + ''.join(word.capitalize() for word in words[1:])
    return cameled
    
        