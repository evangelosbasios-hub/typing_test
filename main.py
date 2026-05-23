#!/usr/bin/env python3
from config import JSON_FILE
from menu import menu, welcome
from utils import clear_terminal, random_value_from_key
from typing_test import typing_test
from stats import calculate_accuracy, calculate_wpm

def run_session(text_key):
    clear_terminal()
    welcome()
    chosen_text = random_value_from_key(JSON_FILE, text_key)
    typed_text, start_time, end_time = typing_test(chosen_text)
    display_results(
        chosen_text,
        typed_text,
        start_time,
        end_time
    )
    input("Press Enter to continue...")

def main():
    while True:
        choice = menu()
        if choice == "exit":
            clear_terminal()
            print("Goodbye!")
            break
        elif choice == "start test":
            run_session("lines")
        elif choice == "practise":
            run_session("paragraphs")

if __name__ == "__main__":
    main()
