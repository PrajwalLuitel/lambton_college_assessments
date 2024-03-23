# Importing the required libraries
import random
import simple_colors as sc
import os


def get_my_man(level):
    """
    This function accepts the level in the hangman game and returns the corresponding structure of the hangman to display.

    Args:
    level: int: the level of the game the user is in

    returns:
    my_man:str: the docstring with the man's figure in it
    """
    if level == 0:
        my_man = """

   ______
   |     |
   |     
   |    
   |     
   |    
   |
  _|_

"""

    elif level ==1:
        my_man = """

   ______
   |     |
   |     O
   |    
   |     
   |    
   |
  _|_

"""
        my_man = sc.green(my_man)

    elif level ==2:
        my_man = """

   ______
   |     |
   |     O
   |     |
   |     
   |    
   |
  _|_

"""
        my_man = sc.green(my_man)

    elif level ==3:
        my_man = """

   ______
   |     |
   |     O
   |    /|
   |     
   |    
   |
  _|_

"""
    elif level ==4:
        my_man = """

   ______
   |     |
   |     O
   |    /|\\
   |     
   |    
   |
  _|_

"""
    elif level ==5:
        my_man = """

   ______
   |     |
   |     O
   |    /|\\
   |     |
   |    
   |
  _|_

"""
        my_man = sc.yellow(my_man)

    elif level ==6:
        my_man = """

   ______
   |     |
   |     O
   |    /|\\
   |     |
   |    / 
   |
  _|_

"""
        my_man = sc.red(my_man)

    elif level ==7:
        my_man = """

   ______
   |     |
   |     O
   |    /|\\
   |     |
   |    / \\
   |
  _|_

"""
        my_man = sc.red(my_man)

    return my_man

def intro():
    """
    This function displays the welcoming message in the game.

    Args:
    none

    Returns:
    none
    """
    # Clearing the screen first
    os.system('clear')
    # Displaying the welcoming text for the game
    welcome_text = sc.blue("Welcome to Hangman !!!", 'bold')
    print(f"""
 {welcome_text}

 \t\t{get_my_man(7)}

\t\t Press any button to Play !!

""")
    # Creating a stopper function for the user to input and begin the game
    start = input()

def get_current_word_state(word, display_indices):
    """
    This function returns the current state of words in the game. i.e. which of the characters to display and which to hide.

    Args:
    word: str : the original word that users are supposed to guess
    display_indices: list[int] : the list of indices from the word which are to be displayed

    Returns:
    word_state: str : the current state of the word that should be displayed

    """
    # Initializing the word state variable
    word_state = ""
    # tracking the elements and indices
    for index, letter in enumerate(word,0):
        # checking the indices to determint whether to show or not
        if index in display_indices:
            word_state += sc.blue(letter, 'underlined')
            word_state += " "
        else:
            word_state += "_" + " "
    # returning the string
    return word_state

def build_screen(man_level, word, hint, display_indices, extra_message=""):
    """
    This function dynamically updates the screen of the hangman game. It clears the previous content and updates with the new one so that it seems dynamic.

    Args:
    man_level : int : it is the level of the man in hangman
    word : str : the word that the player is supposed to guess
    hint : str : the hint given to the player to guess the word
    display_indices : list[int] : the list of indices from the word which are to be displayed
    extra_message : str : an optional message to be shown to the user as per the input

    returns:
    screen : str : a docstring which essentially acts as the screen of the hangman game

    """
    # Clearing the previous content
    os.system("clear")
    # Formulating the docstring according to the arguments
    return f"""
    {extra_message}

    {get_my_man(man_level)}

    
    The HINT is: {sc.green(hint)}

    {get_current_word_state(word, display_indices)}

    Indices: {display_indices}

    """

def get_display_indices(word):
    """
    This function returns the indices to display for the first time when the game starts.

    Args:
    word : str : it is the original word the user has to guess

    Returns:
    display_indices : list[int] : a list containing the indices that is to be displayed
    """
    # we shouldn't display more than the 30% of the total words
    number_given = int(0.3*len(word))
    # Initializing the display indices
    display_indices = []
    # Looping to get the indices
    for i in range(number_given):
        chosen = random.randint(0,len(word)-1)
        # The indices should not be repeated
        if chosen not in display_indices:
            display_indices.append(chosen)
            # The same character shouldn't be left empty, if 'A' is displayed at one place, then it should be at every place
            if word.count(word[chosen]) > 1:
                for index, char in enumerate(word):
                    if char == word[chosen]:
                        display_indices.append(index)
    # returning the list of integers
    return list(set(display_indices))

def update_indices(word, display_indices, char):
    """
    This function updates the indices of the original word to be displayed everytime the user provides the guess.

    Arguments:
    word: str : the original word that the user has to guess
    display_indices : list[int] : the indices of the word of which the characters are to be displayed in the screen
    char : str : the character provided by the user
    
    Returns:
    display_indices : list[int] : the indices of the original word of which the characters have been found so far
    """
    # mapping elements and indices
    for index, el in enumerate(word):
        if char == el and index not in display_indices:
            display_indices.append(index)

    # returning the appropriate indices to display
    return display_indices

# The main driver code
if __name__ == "__main__":
    # The introductory screen
    intro()

    # Creating a list of possible words in the game
    possible_words:list[str] = ["HELLO", "WORLD", "PYTHON", "LAMBTON", "REACT", "JAVASCRIPT", "JAVA", "SWITZERLAND" ]
    # A parallel array for the hints to the words above
    hints:list[str] = ["A greeting in English", "Where do we live?", "The best programming language", "A college in Canada", "A web library built by Meta", "A web programming language", "A programming language which is targeted for vulnerability", "A great country to live in Europe!!"]

    # key: value mapping of the words and hints
    word_and_hint = dict(zip(possible_words, hints))

    # randomly choose a word from the above possible words
    word:str = random.choice(possible_words)
    
    # Initially, the man is at level 0 in the game
    my_man_level:int = 0
    # Getting the initial indices for the characters to display for the users to guess
    display_indices:list[int] = get_display_indices(word)
    # Any extra message for the user
    extra_message = ""
    
    while my_man_level < 7:
        # Building the screen with all parameters and displaying it to the user
        print(build_screen(my_man_level, word, word_and_hint[word], display_indices, extra_message))
        # Getting the choice from the user
        user_chosen:str = input("Try guessing the letters: ")
        # Converting the user chosen character to uppercase
        user_chosen = user_chosen.upper()

        # Checking whether the user chosen character is in the original word
        if user_chosen in word:
            # Checking if the word user has chosen is already displayed
            if word.index(user_chosen) in display_indices:
                extra_message = sc.yellow("\tIt's already there!! Choose another one")
                continue
            else:
                # Updating the user chosen character in the display_indices array
                display_indices = update_indices(word, display_indices, user_chosen)
                # Creating message for the user
                extra_message = sc.green("\tYou got it right !!")

                # Winning condition and messages
                if len(display_indices) == len(word):
                    extra_message = sc.green("\t\tYou WON the game !!!!!!!! Voilaaa !!!", 'bold')
                    print(build_screen(my_man_level, word, word_and_hint[word], display_indices, extra_message))
                    break

        else:
            # The user fails to guess the correct letters
            extra_message = sc.red("\tOops, Not There !!", 'bold')
            my_man_level += 1
            # Losing condition for the game and the messages for that
            if my_man_level >=7:
                extra_message = sc.red("\t\tYou FAILED to win the game, Better Luck Next Time. . .")    
                print(build_screen(my_man_level, word, word_and_hint[word], display_indices, extra_message))
                break
            