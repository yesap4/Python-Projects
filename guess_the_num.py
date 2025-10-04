import random

def guess_the_number():
    number = random.randint(1, 100)
    max_attempts = 10
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempt} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")

if __name__ == "__main__":
    guess_the_number()
