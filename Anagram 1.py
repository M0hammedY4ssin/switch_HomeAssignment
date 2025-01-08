'''
Anagrams
How do you check if two strings are anagrams of each other?
Anagrams are words or phrases formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
Examples:
"listen" → "silent"
"earth" → "heart"
'''

def is_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    letters = [0] * 26
    for c in word1:
        letters[ord(c) - ord('a')] += 1
    for c in word2:
        letters[ord(c) - ord('a')] -= 1
    
    for l in letters:
        if l != 0: 
            return False
    return True

print(is_anagrams("listen", "silent"))
print(is_anagrams("listten", "silent"))
print(is_anagrams("earth", "heartr"))