#!/usr/bin/env python3
import random
import json
import os
import sys
import time
import tty
import termios

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "sentences.json")
# Colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def clear_terminal():
    os.system("clear")


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
        print("2. Exit")
        print()

        choice = input("Choose an option: ")

        if choice == "1":
            return "start"

        elif choice == "2":
            return "exit"

        else:
            print()
            print("Invalid choice.")
            time.sleep(1)

def random_line(json_file, key):
    with open(json_file, "r") as file:
        data = json.load(file)

    return random.choice(data[key])


def calculate_accuracy(target, typed):
    correct = 0

    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct += 1

    return (correct / max(len(target), len(typed))) * 100


def calculate_wpm(target, typed, elapsed_time):
    correct_chars = 0

    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct_chars += 1

    minutes = elapsed_time / 60

    if minutes <= 0:
        return 0

    return (correct_chars / 5) / minutes


def typing_test(chosen_text):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    typed_text = ""

    try:
        print(chosen_text)
        print()

        tty.setraw(fd)

        # Wait for first key
        first_key = sys.stdin.read(1)

        start_time = time.perf_counter()

        if first_key not in ("\r", "\n"):
            typed_text += first_key

            if first_key == chosen_text[0]:
                sys.stdout.write(GREEN + first_key + RESET)
            else:
                sys.stdout.write(RED + first_key + RESET)

            sys.stdout.flush()

        while True:
            key = sys.stdin.read(1)

            # Enter key ends test
            if key in ("\r", "\n"):
                break

            # Backspace
            elif key == "\x7f":
                if len(typed_text) > 0:
                    typed_text = typed_text[:-1]

                    sys.stdout.write("\b \b")
                    sys.stdout.flush()

            else:
                # Stop at sentence length
                if len(typed_text) >= len(chosen_text):
                    break

                expected_char = chosen_text[len(typed_text)]

                typed_text += key

                # Correct character
                if key == expected_char:
                    sys.stdout.write(GREEN + key + RESET)

                # Incorrect character
                else:
                    sys.stdout.write(RED + key + RESET)

                sys.stdout.flush()

        end_time = time.perf_counter()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return typed_text, start_time, end_time


def display_results(target, typed, start_time, end_time):
    elapsed_time = end_time - start_time

    accuracy = calculate_accuracy(target, typed)
    wpm = calculate_wpm(target, typed, elapsed_time)

    print()
    print("========== RESULTS ==========")
    print(f"Time: {elapsed_time:.2f} seconds")
    print(f"WPM: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typed text: {typed}")
    print("=============================")


def main():
    while True:
        choice = menu()

        if choice == "exit":
            clear_terminal()
            print("Goodbye!")
            break

        elif choice == "start":
            clear_terminal()

            welcome()

            chosen_text = random_line(JSON_FILE, "lines")

            typed_text, start_time, end_time = typing_test(chosen_text)

            display_results(
                chosen_text,
                typed_text,
                start_time,
                end_time
            )

            print()
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
