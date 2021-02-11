#!/usr/bin/python3

from time import sleep
import twl


WORDS = set(twl.iterator())
LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2,
                 "e": 1, "f": 4, "g": 2, "h": 4,
                 "i": 1, "j": 8, "k": 5, "l": 1,
                 "m": 3, "n": 1, "o": 1, "p": 3,
                 "q": 10, "r": 1, "s": 1, "t": 1,
                 "u": 1, "v": 4, "w": 4, "x": 8,
                 "y": 4, "z": 10}
starting_text = "X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0"
TEST = True


test = list(twl.anagram('screwinga'))
nine = list()
eight = list()
seven = list()
six = list()

for x in test:
    if len(x) == 9:
        nine.append(x)
    elif len(x) == 8:
        eight.append(x)
    elif len(x) == 7:
        seven.append(x)
    elif len(x) == 6:
        six.append(x)

if len(nine) > 0:
    print(nine)
else:
    print("No nine letter words found")

print(eight)
print(seven)
print(six)

# def get_scrabble_words():
#     print("Getting Scrabble Dictionary...")
#     return WORDS
