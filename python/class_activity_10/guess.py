import random
import simple_colors as sc

if __name__ == "__main__":
    # Initializing the game
    print(sc.blue("\tWelcome to the number Guessing game !!!!\n\n", 'bold'))

    # randomly choosing an integer between 0 to 20 
    chosen_number = random.randint(0,20)
    # Counting the attempts of the user
    attempts = 0

    # We allow the users with unlimited attempts to guess the number
    while True:
        # Getting input from the user
        user_guess = int(input("Please guess your number: "))
        # Incrementing the attempt of the user after every guess
        attempts += 1

        # Checking the criteria and replying accordingly
        if user_guess < chosen_number:
            print(sc.yellow("\tYour number is lower than the expected value !"))

        elif user_guess > chosen_number:
            print(sc.red("\tYour number is higher than the expected value !"))
        
        else:
            print(sc.green(f"\tYou are able to exactly guess the number !!!! in {attempts} attempts", 'bold'))
            # After the guess is successful, ending the game by getting out of the loop
            break
