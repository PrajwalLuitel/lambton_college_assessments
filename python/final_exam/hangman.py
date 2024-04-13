import random
import datetime
### Class Template

class HangmanGame:
    # Class attribute for hangman stages
    hangman_stages = [
    # Initial empty stage
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    # First wrong guess (head)
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    # Second wrong guess (body)
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    # Third wrong guess (one arm)
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    # Fourth wrong guess (both arms)
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    # Fifth wrong guess (one leg)
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    # Final stage (both legs, game over)
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]
    def __init__(self, player_name, student_id, word, hint):
        # Initialize game state
        self.player_name = player_name
        self.student_id = student_id

        self.word = word.lower()
        self.hint = hint
        self.guessed_letters = set([])

        self.current_hangman_stage = 0
        self.game_over = False



    def ask_for_guess(self):
        # Prompt player to guess a letter
        user_guess = input("Guess a letter: ")
        return user_guess


    def check_guess(self,user_guess):
        # Check if the guessed letter is in the secret word
        user_guess = user_guess.lower()
        if user_guess in self.word:
            self.guessed_letters.add(user_guess)
            return True
        else:
            return False


    def update_display(self,hangman_stages = hangman_stages):
        # Update the display of the guessed letters and hangman drawing
        print(hangman_stages[self.current_hangman_stage])
        print(f"The hint is: {self.hint}")
        forming_string = ""
        for el in self.word:
            if el in self.guessed_letters:
                forming_string+= el+" "
            else:
                forming_string += " _ "
        print(f"The status so far: {forming_string}")


    def play(self):
        # Main game loop
        while not self.game_over:
            self.update_display()
            guess = self.ask_for_guess()
            if not self.check_guess(guess):
                self.current_hangman_stage+=1
                if self.current_hangman_stage >= 6:
                    self.game_over = True
            if set(self.word) == self.guessed_letters:
                self.game_over = True
        
        if self.game_over:
            if self.current_hangman_stage >=6:
                self.update_display()
                print("You lost the game !!!")
            else:
                self.update_display()
                print("You won the game !!!!!")



    def calculate_game_duration(self, start, end):
        # Calculate and display the game duration
        duration = end-start
        print(f"The game ran for {duration} seconds.")


if __name__ == "__main__":
    username = input("Please enter your name: ")
    userid = input("Please enter your student id: ")

    my_words = [{'canada':'A beautiful country known for cold weather.' },{'python':'a user-friendly programming language'},{'notebook':'a hollywood movie'}]

    choice_dict = random.choice(my_words)
    word = list(choice_dict.keys())[0]
    hint = choice_dict[word]

    my_hangman = HangmanGame(username, userid, word, hint)
    start = datetime.datetime.now()
    my_hangman.play()
    end = datetime.datetime.now()
    my_hangman.calculate_game_duration(start, end)
    



