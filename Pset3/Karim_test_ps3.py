from ps3 import *

WORDLIST_FILENAME = "words.txt"

word_list = load_words()
word = "h*llo"
hand = {"h":1, "e":1, "l":2, "o":1}
print(is_valid_word(word,hand,word_list))
substitute_hand(hand, "e")
print()
print()
substitute_hand(hand,"l")