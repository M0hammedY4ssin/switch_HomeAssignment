'''
Anagrams 2
How do you check if two strings are anagrams with 1 mistake.
A mistake can be:
missing letter:  abc, ba
1 replacement:   abc, cna
'''

def is_anagrams(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False
    letters = [0] * 26
    for c in word1:
        letters[ord(c) - ord('a')] += 1
    for c in word2:
        letters[ord(c) - ord('a')] -= 1
    sum = 0
    for l in letters:
        sum += abs(letters[l])

    if sum > 1:
        return False
    return True

print(is_anagrams("listen", "silent"))
print(is_anagrams("listten", "silent"))
print(is_anagrams("earth", "heart"))
print(is_anagrams("abc", "ba"))
print(is_anagrams("abc", "cna"))
print(is_anagrams("abc", "aaa"))