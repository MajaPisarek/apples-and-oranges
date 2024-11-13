#
#           project:    applesandoranges.py
#            authors:    Maja Pisarek and Eliana Louis-Jean
#           version:    10/16/24
#
#   description: A version of the game "Mastermind"




# Start by introducing the game and sharing an overview of the rules.
print("""

Welcome to apples and oranges!
This is a challenge in which the gatekeeper, Player 1, creates a three-digit, secret code.
  The three digits must be unique and use the numbers 0 through 9.

Then, the keymaster, Player 2, must  crack the code. They have 10 tries
  to guess the three-digit code and will receive a score from the gatekeeper.

Scoring:
Banana: None of the digits in your guess are in the secret code.
[A}pple: One digit in your guess is correct and in the correct position of the secret code. 
  Please note that if you have three Frogs, you win and may lead a victory dance of one lap about the room!
[O]range: One digit of your guess is present in the secret code, but in the wrong position.
  If you get three Oranges, your guess has all the correct digits, but in the wrong places!

""")

# Get names of contestants
# Player 1 is the gatekeeper. Get their name and their secret code.
name1 = input("gatekeeper, what is your name? : ")
code = input("Now enter your secret, three-digit code: ")

print(""".
..
...
..
.
..
...
..
.
..
...
..
.
..
No looking!""")

# Player 2 is the keymaster. Ask their name and their guess.
# They get 10 tries to break the code.
name2 = input("keymaster, what is your name? : ")

hasWon = False
numberOfGuesses = 0
while hasWon is False :
    guess = input("Enter your guess of the code: ")
    numberOfGuesses += 1

    # Have Player 1 score Player 2's guess.
    score = input("Now the Gatekeeper will score your guess: ")

    # Display the turn number, the guess, and the score
    if score == "FFF" :
        print(f"Your guess of {guess} is correct! You won in {numberOfGuesses} guesses.")
        hasWon = True
    else :
        print(f"Your guess was: {guess} and you scored: {score}. You have {10-numberOfGuesses} left.")
    # Repeat until Player 2 gets it right or has used all 10 tries.
