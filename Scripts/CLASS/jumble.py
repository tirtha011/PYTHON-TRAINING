import random

def jumble_word(word):

    char = list(word.upper())

    random.shuffle(char)

    jumbled_word = "".join(char)

    return ' '.join(jumbled_word)

word = input("Enter a word to jumble: ")

jumbled_word = jumble_word(word)

print("The jumbled word is:", jumbled_word)