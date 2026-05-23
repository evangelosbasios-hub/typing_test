import os
import json
import random

def clear_terminal():
    os.system("clear")

def random_value_from_key(json_file, key):
    with open(json_file, "r") as file:
        data = json.load(file)

    return random.choice(data[key])