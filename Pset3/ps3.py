# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    lower_word = word.lower()

    let_scores = [SCRABBLE_LETTER_VALUES[x] for x in lower_word if x in SCRABBLE_LETTER_VALUES.keys() ]
    comp_1 = sum(let_scores)
    word_len = len(word) 
    comp_2 = max(7*word_len-3*(n-word_len),1) 
    return comp_1*comp_2
    

    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    #include 1 wildcard character *
    hand['*'] = 1

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    word_lower = word.lower()
    for letter in word_lower:
        if letter in new_hand.keys():
            new_hand[letter] -= 1
        
    return new_hand
    

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # First we check if word is actually a valid word in word_list
    word_lower = word.lower()
    possible_list = [word_lower]

    #if * is used --> make a list of all possible words that substitute * for a vowel
    if '*' in word_lower:
        idx  = word_lower.find('*')
        possible_list = []
        
        word_let = [char for char in word_lower]
        for vowel in VOWELS:
            possible_word = word_let
            possible_word[idx] = vowel 
            possible_list.append(''.join(possible_word))

    #negative counter to check how many words are not in word_list

    neg_counter = 0
    for pos_word in possible_list:

        if pos_word not in word_list:
            neg_counter +=1
        else:
            temp_word = pos_word
            print(f'this is working and the word is {temp_word}')
            break
    if neg_counter == len(possible_list):
        return False

    
    # Check if hand letters support word. 
    word_dic = {}
    for letter in word_lower:
        if letter != "*":
            word_dic[letter] = word_dic.get(letter,0) + 1
        for letter in word_dic.keys():
            if word_dic[letter]>hand.get(letter,0):
                return False
    return True





 
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for key in hand.keys():
        count += hand[key]
    return count
    

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    
    # Keep track of the total score
    score = 0 
    # As long as there are still letters left in the hand:

    temp_hand = hand.copy()
    hand_len = calculate_handlen(temp_hand)
    while hand_len > 0:

        # Display the hand
        display_hand(temp_hand)

        # Ask user for input
        usr_in = input("Enter word, or \"!!\" to indicate that you are finished: ")
        # If the input is two exclamation points:
        if usr_in == "!!":
            # End the game (break out of the loop)
            print(f"Total score: {score}")
            break     
            
        # Otherwise (the input is not two exclamation points):
        else:   
            # If the word is valid:
            if is_valid_word(usr_in, temp_hand,word_list):
                # Tell the user how many points the word earned,

                word_score = get_word_score(usr_in,hand_len)
                print(f"\"{usr_in}\" earned {word_score} points.", end = " ")
                # and the updated total score
                score += word_score
                print(f"Total: {score} points")

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            temp_hand = update_hand(hand = temp_hand, word = usr_in)
            hand_len = calculate_handlen(temp_hand)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print(f"Total score: {score}")
    # Return the total score as result of function
    return score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    sub_hand = dict(hand)
    let_in_hand = sub_hand.keys()
    if letter not in let_in_hand:
        return None

    unused_letters = [char for char in SCRABBLE_LETTER_VALUES.keys() if char not in let_in_hand]
    
    sub_letter = random.choice(unused_letters)
    

    sub_hand[sub_letter] = sub_hand.pop(letter)

    
    return sub_hand





    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    num_rounds = int(input("How many hands would you like to play: "))
    round_hand = deal_hand(HAND_SIZE)
    
    for round in range(num_rounds):
        
        temp_hand = dict(round_hand)


        print("Current hand: ")
        for char in temp_hand: print(char, end = " ")
        print()
        to_substitute = input("Would you like to substitute a letter: ")
        if to_substitute.lower() == "yes": 
            sub_let = input("Which letter would you like to substitute: ")
            temp_hand = substitute_hand(temp_hand, sub_let)
            print("Current hand: ")
            for char in temp_hand: print(char, end = " ")
            print()
        play_hand(temp_hand, word_list)
        print("-------------------")
        replay_hand = input("Would you like to replay your hand: ")
        if replay_hand.lower() == "yes":
            pass
        else:
            round_hand = deal_hand(HAND_SIZE)


        



#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

   