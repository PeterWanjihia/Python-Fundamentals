import random

def computer_guess_number(min_value, max_value):
    attempts = 0

    while True:
        guess = (min_value + max_value) // 2
        print(f"Computer guesses: {guess}")
        attempts += 1

        response = input("Is the guess correct? (Enter 'c' for correct, 'h' for too high, 'l' for too low): ").lower()

        if response == 'c':
            print(f"Computer guessed the correct number {guess} in {attempts} attempts.")
            break
        elif response == 'h':
            max_value = guess - 1
        elif response == 'l':
            min_value = guess + 1
        else:
            print("Invalid input. Please enter 'c', 'h', or 'l'.")

def main():
    print("Think of a number between 1 and 100 (inclusive).")
    min_value = 1
    max_value = 100
    computer_guess_number(min_value, max_value)

if __name__ == "__main__":
    main()
