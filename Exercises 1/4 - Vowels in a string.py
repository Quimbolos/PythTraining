import math

def VowelCounter(Word):

 lowercase = Word.lower()

 vowel_counts = {}

 for vowel in "aeiou":

    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
 
 print(vowel_counts)

Word = str(input("Enter your word: "))

VowelCounter(Word)