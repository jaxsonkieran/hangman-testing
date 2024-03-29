import random

# Function to choose a random word from a list
def choose_word():
    word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "strawberry"]
    return random.choice(word_list)

# Function to display the hangman
def display_hangman(lives):
    stages = [  
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    if lives < len(stages):
        return stages[lives]
    else:
        return stages[-1]  # Return the last stage if lives exceed the length of stages

# Function to check if the guessed letter is in the word
def check_guess(word, guessed_letters, guess):
    if guess in guessed_letters:
        print("You already guessed this letter.")
        return False
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

# Function to display the word with blanks and guessed letters
def display_word(word, guessed_letters, incorrect_guesses):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_ "
    displayed_word += "\nIncorrect guesses: " + ", ".join(incorrect_guesses)
    return displayed_word
    
# Function to check if the guessed word matches the chosen word
def check_word_guess(word, guessed_word):
    if guessed_word == word:
        return True
    else:
        return False

# Function to play the hangman game
def hangman():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    
    print("Choose difficulty:")
    print(" - Enter 'e' for easy (8 lives)")
    print(" - Enter 'm' for medium (6 lives)")
    print(" - Enter 'h' for hard (4 lives)")
    
    difficulty = input("Enter your choice (e/m/h): ").lower()
    if difficulty == "e":
        lives = 8
    elif difficulty == "m":
        lives = 6
    elif difficulty == "h":
        lives = 4
    else:
        print("Invalid input. Defaulting to easy.")
        lives = 8
    
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = []
    game_over = False
    
    while not game_over:
        print(display_hangman(lives))
        print(display_word(word, guessed_letters, incorrect_guesses))
        guess = input("Guess a letter or the entire word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter.")
                continue
            if guess in word:
                guessed_letters.append(guess)
                if ''.join(guessed_letters) == word:
                    print(display_hangman(lives))
                    print(display_word(word, guessed_letters, incorrect_guesses))
                    print("Congratulations! You guessed the word correctly!")
                    game_over = True
            else:
                incorrect_guesses.append(guess)
                lives -= 1
                print(f"You have {lives} lives remaining.")
                if lives == 0:
                    print("You're out of lives! The word was:", word)
                    game_over = True
        elif len(guess) > 1 and guess.isalpha():
            if check_word_guess(word, guess):
                print(display_hangman(lives))
                print(display_word(word, guessed_letters, incorrect_guesses))
                print("Congratulations! You guessed the word correctly!")
                game_over = True
            else:
                print("Incorrect guess!")
                lives -= 1
                print(f"You have {lives} lives remaining.")
                if lives == 0:
                    print("You're out of lives! The word was:", word)
                    game_over = True
        else:
            print("Please enter a single alphabetical character or the entire word.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing!")

# Start the game
hangman()