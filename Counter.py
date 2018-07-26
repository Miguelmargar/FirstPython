from collections import Counter

def anagram():
    word1 = "hello"
    word2 = "hello"
    print(Counter(word1) == Counter(word2))
    
anagram()