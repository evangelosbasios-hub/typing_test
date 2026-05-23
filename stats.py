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