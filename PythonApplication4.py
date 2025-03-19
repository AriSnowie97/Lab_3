print("Task #2 by Arina Badovska")
import random
import tkinter as tk
from tkinter import messagebox

def generate_secret_code(unique=True):
    digits = list(range(10))
    if unique:
        random.shuffle(digits)
        return digits[:4]
    else:
        return [random.randint(0, 9) for _ in range(4)]

def evaluate_guess(secret_code, guess):
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if digit == secret_code[i]:
            bulls += 1
        elif digit in secret_code:
            cows += 1
    return bulls, cows

class CodeGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Game Secret Code")
        self.secret_code = generate_secret_code()
        self.attempts = 0
        self.label = tk.Label(master, text="Enter 4-digit code:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.button = tk.Button(master, text="Enter", command=self.check_guess)
        self.button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = [int(digit) for digit in self.entry.get()]
            if len(guess) != 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter 4-digit code.")
            return

        self.attempts += 1
        bulls, cows = evaluate_guess(self.secret_code, guess)
        self.result_label.config(text=f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            messagebox.showinfo("Congrats!", f"You guessed the code by {self.attempts} attempts.")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = CodeGuessingGame(root)
    root.mainloop()
