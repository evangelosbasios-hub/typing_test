import sys
import tty
import termios
import time

from config import RED, GREEN, RESET
def typing_test(chosen_text):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    typed_text = ""

    try:
        print(chosen_text)
        print()
        tty.setraw(fd)
        start_time = time.perf_counter()
        while True:
            key = sys.stdin.read(1)
            # Ctrl + C
            if key == "\x03":
                raise KeyboardInterrupt
            # Handle Enter
            if key in ("\r", "\n"):
                key = "\n"
                # Stop if text is complete
                if len(typed_text) >= len(chosen_text):
                    break

                expected_char = chosen_text[len(typed_text)]
                typed_text += key
                # Move cursor correctly
                sys.stdout.write("\r\n")
                sys.stdout.flush()

                continue
            # Handle Backspace
            elif key == "\x7f":
                if len(typed_text) > 0:
                    typed_text = typed_text[:-1]

                    sys.stdout.write("\b \b")
                    sys.stdout.flush()

                continue
            # Stop when all text is typed
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
    except KeyboardInterrupt:
        print("\nExiting typing test...")
        end_time = time.perf_counter()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return typed_text, start_time, end_time