import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.guesses_remaining = 10

        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 18), width=5)
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

    def check_guess(self):
        user_guess = int(self.entry.get())
        self.guesses_remaining -= 1

        if user_guess < self.target_number:
            self.result_label.config(text=f"Too low! Guesses remaining: {self.guesses_remaining}")
        elif user_guess > self.target_number:
            self.result_label.config(text=f"Too high! Guesses remaining: {self.guesses_remaining}")
        else:
            self.result_label.config(text="Congratulations! You guessed the number!")
            self.submit_button.config(state=tk.DISABLED)
        if self.guesses_remaining == 0 and user_guess != self.target_number:
            self.result_label.config(text=f"Out of guesses! The number was {self.target_number}")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
