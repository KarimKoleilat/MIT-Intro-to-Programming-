
# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    temp_word = [char for char in secret_word]
    for let in letters_guessed: 
        while let in temp_word:
            temp_word.remove(let)
    if len(temp_word) ==0:
        return True
    else:
        return False





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    template = ["_ " for let in secret_word]
    for let in letters_guessed:
        if let in secret_word:
            indexes = [i for i,x in enumerate(secret_word) if x == let]
            
            
            for idx in indexes: template[idx] = let
            

    return "".join(elem for elem in template)

lets_g = ['a','b','d','c']
sec_w = "abcccddd"
#print(is_word_guessed(sec_w,lets_g))
#print(get_guessed_word(sec_w,lets_g))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_available = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    
    
    for let in letters_guessed:
        if let in letters_available:
            indexes = [i for i,x in enumerate(letters_available) if x == let]
            for idx in indexes: letters_available[idx] = "_ "
    return letters_available




    
secret_word = "hello"    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    word_len = len(secret_word)
    guesses = 3
    guessed_word = get_guessed_word(secret_word,[])
    letters_guessed = []
    print(f"The secret word contains {word_len} letters and you have {guesses} guesses left!")
    print("Please guess one letter at a time")
    alphabet_letters = get_available_letters([])
    unique_letters = 0
    secret_list = [char for char in secret_word]
    for char in secret_list:
    	if char not in unique_letters:
    		unique_letters +=1


    while(guesses>0):
        
        guessed_letter = input("Guess a letter!")
        #while loop to make sure guess is valid
        while (guessed_letter not in alphabet_letters):
            guessed_letter = input("Oops, that's not a valid guess, guess again!")
        #letter guess has not been guessed before
        while(guessed_letter in letters_guessed):
            guessed_letter = input("You guessed that letter already, guess another one!")
        
        letters_guessed.append(guessed_letter)
        let_avail = get_available_letters(letters_guessed)

        #conditional updating the guessed_word variable and instructing the player further.
        if guessed_letter in secret_word:
            guessed_word = get_guessed_word(secret_word,letters_guessed)
            print(f"Nice Guess! Here's what you guessed so far {guessed_word}")
        
        elif guessed_letter not in secret_word:
            print(f"Better luck next guess! Here's what you guessed so far {guessed_word}")
            guesses -= 1

        print(f"you have {guesses} left!")

        if (is_word_guessed(secret_word, letters_guessed)):
            print("You guessed it!!!")
            score = guesses*unique_letters
            break
        elif(guesses ==0 and not is_word_guessed(secret_word,letters_guessed)):
            print("You didn't make it! play again?!")
            print(f"the word is {secret_word}")
            break

            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    #first checks if lengths are the same
    alphabet_letters = get_available_letters([])
    temp_word = my_word
    temp_word = temp_word.replace("_ ", "*")
    if len(temp_word) != len(other_word):
    	return False

    #initializes a temporary place holder for the guessed word so far and replaces the "_ " with "*" for ease of indexing and comparison with other_word
    

    #loop over my_word and return false if there is a discrepancy
    #ignores the comparison if the char in my_word is a *
    for idx in range(len(temp_word)):
    	if temp_word[idx] == "*":
    		print(f"this is a star {temp_word[idx]}")
    		pass
    	elif temp_word[idx] != other_word[idx]:
    		print(f"this is a false letter not matching {temp_word[idx]}")
    		return False
    #if all are cleared and no false --> return True
    return True


wrd = "a_ _ le"
other_word = "apple"
print(match_with_gaps(wrd, other_word))





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_matches = []
    word_list = load_words()
    for word in word_list:
    	if match_with_gaps(my_word,word):
    		list_of_matches.append(word)
    return list_of_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)