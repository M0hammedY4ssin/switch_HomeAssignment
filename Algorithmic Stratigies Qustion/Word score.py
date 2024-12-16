'''
Word Score
Given a string of words, you need to find the highest scoring word. 
Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
○	You need to return the highest scoring word as a string.
○	If two words score the same, return the word that appears earliest in the original string.
○	All letters will be lowercase and all inputs will be valid.

'''
def word_score(words):
    max_score=0
    highest_scoring_word = ""

    for word in words:
        score = calculate_score(word)
        if score > max_score:
            max_score= score
            highest_scoring_word = word
       
    return highest_scoring_word

def calculate_score(word):
    score_val=0
    
    for c in word:
        score_val += ord(c) - ord('a') + 1

    return score_val