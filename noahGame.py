import random

def get_difficulty():
    level = input("Choose difficulty - easy, medium, or hard: ").lower()

    match level:
        case "easy":
            difficulty =  10
        case "medium":
            difficulty = 7
        case "hard":
            difficulty = 5
        case _:
            print("Unknown level")
            get_difficulty()
    print(difficulty)
    return difficulty

    # if level == "easy":
    #     return 10
    # elif level == "medium":
    #     return 7
    # else:
    #     return 5
def pointDeduction(numOfGuesses):
    deduction =  100 / numOfGuesses
    print(f" {deduction: .2f}")
    return (f"{deduction: .2f}")
def play_game():
    secret = random.randint(1, 100)
    guesses_left = get_difficulty()
    deduction = pointDeduction(guesses_left)
    print(f"This is deduction: {deduction}") 
    print(f"I have {guesses_left} attempts to guess the secret number!")

    #declared variables
    # numOfGuesses = 0 
    yourGuess = 0
        
    for numOfGuesses in range(0, guesses_left):
        print(f"The secret number is : {secret}")
        yourGuess = int(input("Guess a Number: "))     # if the nummber is greater than the guess you have in mind
        if secret > yourGuess:
           print(f"I have guessed {yourGuess}. Guess higher\n")
        
        #  if the number is lower than what you have in mind
        elif secret < yourGuess:
            print(f"I have guessed {yourGuess}. Guess lower\n")
        
        # #  the computer guessed your number!
        else:
            print(f"I've won {yourGuess}!")
            total = 100 - float(deduction * numOfGuesses)
            print(total)
            break
    # print(numOfGuesses +1)
    if guesses_left == numOfGuesses +1:
        print(f"You used all your {guesses_left} guesses")
if __name__ == "__main__":
    play_game()