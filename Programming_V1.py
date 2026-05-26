import random

# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instruction():
    print('''
**** Instructions ****
To begin, choose the number of rounds. 
Your goal is to try to solve the equation.
Good luck.
''')


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."
        try:
            response = int(input(question))
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Main Routine
print("➕➖ Welcome to the Basic Math Quiz ➗✖️\n")

if yes_no("Do you want to read the instructions? ") == "yes":
    instruction()

num_rounds = int_check("How many rounds would you like to play? ")
rounds_played = 0

# list history
game_history = []
score = 0


while rounds_played < num_rounds:
    print(f"\nRound {rounds_played + 1} of {num_rounds}")

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    symbol = random.choice(['+', '-', '*', '/'])

    # For clean numbers and answers
    if symbol == '/':
        num1 = num2 * random.randint(1, 10)
        correct_answer = num1 // num2
    elif symbol == '*':
        correct_answer = num1 * num2
    elif symbol == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    try:
        user_answer = int(input(f"Solve: {num1} {symbol} {num2} = "))
        if user_answer == correct_answer:
            print("Correct! ✅")
        else:
            print(f"Incorrect ❌. The correct answer is {correct_answer}.")
        rounds_played += 1  # Continue only if input is valid
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("\nThanks for playing!")









