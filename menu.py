import time
from utils import clear_terminal

def welcome():
    print("Welcome to the typing tester")
    print("Type the sentence correctly and as fast as you can")
    print("When you finish, WPM, time, and accuracy will be shown")
    print()

def menu():
    while True:
        clear_terminal()

        print("===== TYPING TESTER =====")
        print("1. Start typing test")
        print("2. Start practising text")
        print("3. Exit the application")
        print()

        choice = input("Choose an option: ")

        if choice == "1":
            return "start test"
        elif choice == "2":
            return "practise"
        elif choice == "3":
            return "exit"

        print("\nInvalid choice.")
        time.sleep(1)