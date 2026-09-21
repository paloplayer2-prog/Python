import tkinter as tk
import random

secret_number = random.randint(1, 100)
tries = 0

window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("600x600")
window.config(bg="#f0f0f0")

def restart_game():
    global secret_number, tries
    
    
    secret_number = random.randint(1, 100)
    tries = 0
    
    
    result_label.config(text="Guess!")
    
    
    guess_box.delete(0, tk.END)
    
    guess_button.config(state=tk.NORMAL)

def check_guess():
    global tries
    guess = int(guess_box.get())
    tries += 1

    if guess > secret_number:
        result_label.config(text="Too high! Try again.")
    elif guess < secret_number:
        result_label.config(text="Too low! Try again.")
    else:
        result_label.config(text=f"Congratulations! You've guessed the number {secret_number} in {tries} tries.")
        guess_button.config(state=tk.DISABLED)
guess_box = tk.Entry(window, font=("Arial", 14), justify="center", bg="white", fg="black", bd=2, relief="solid")
guess_box.pack(pady=10)

result_label = tk.Label(window, text="Guess!", font=("Arial", 14))
result_label.pack(pady=10)

guess_button = tk.Button(window, text="Guess", command=check_guess, font=("Arial", 14))
guess_button.pack(pady=10)

restart_button = tk.Button(
    window, 
    text="🔄 Play Again", 
    command=restart_game, 
    font=("Arial", 12),
    bg="#e0e0e0"
)
restart_button.pack(pady=5)

instructions_label = tk.Label(window, text="Guess a random number between 1 and 100.", font=("Arial", 12))
instructions_label.pack(pady=10)

window.mainloop()