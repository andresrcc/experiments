import random


def guess_the_number():
    random_number = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")

    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        try:
            user_input = int(input("Guess the number:"))
        except ValueError:
            print("Invalid input, please enter an integer")
            continue

        if user_input > 100 or user_input < 0:
            print("Please enter a number between 1 and 100")
            continue

        attempts += 1

        if random_number == user_input:
            print("You guessed right!")
            break
        elif user_input < random_number:
            print("Too low!")
        else:
            print("Too high! ")

def main():
    while True:
        guess_the_number()
        play_again = input("Would you like to play again? (yes/no)").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()