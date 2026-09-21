def add_notebook():
    notebook = input("\nWhat do you want to note down? ")
    with open("journal.txt", "a") as file:
        file.write(notebook + "\n")
    print("✅ Note saved!\n")


def read_notebook():
    print("\n--- 📖 YOUR NOTES ---")
    with open("journal.txt", "r") as file:
        notes = file.read()  # Added () here!
        print(notes)
    print("---------------------\n")


# 🔁 Keep the app running in a loop:
while True:
    print("1: Write a note")
    print("2: Read notes")
    print("3: Exit")
    
    choice = input("What would you like to do? ")

    if choice == "1":
        add_notebook()
    elif choice == "2":
        read_notebook()
    elif choice == "3":
        print("Goodbye! 👋")
        break  # 'break' immediately stops the while loop!
    else:
        print("Invalid choice, please choose 1, 2, or 3.\n")