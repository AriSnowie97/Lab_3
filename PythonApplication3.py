print("Task #1 By Arina Badovska")
import random
import secrets

def generate_secret_code(unique=True):
    digits = list(range(10))
    if unique:
        random.shuffle(digits)
        return digits[:4]
    else:
        return [random.choice(0,9) for _ in range(4)]
def evaluate_guess(secret_code, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1
    return bulls, cows
def play_game():
    secrets = generate_secret_code()
    attempts=0
    print("Welcome to the game of Bulls and Cows!")
    print("Try to guess the 4-digit secret code.")
    while True:
        guess = input("Enter your guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid guess. Please enter a 4-digit number.")
            continue
        guess = [int(d) for d in guess]
        bulls, cows = evaluate_guess(secrets, guess)
        attempts += 1
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print(f"Congratulations! You've guessed the secret code in {attempts} attempts.")
            break
if __name__ == "__main__":
    play_game()
