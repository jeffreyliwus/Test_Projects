import random


def mask_word(word, computer_action):
    return "".join([letter if letter in computer_action else "*" for letter in word])


mask_char = "*"
possible_word = [
    "cat",
    "sun",
    "cup",
    "ghost",
    "flower",
    "pie",
    "cookie",
]
computer_action = random.choice(possible_word)
print(computer_action)

word = str(input("player my guess the word, enter a letter: "))

if word in computer_action:
    print("correct!")

    print("        __________")
    print("       |")
    print("       |")
    print("       |")
    print("       |")
    print("       -")

    masked_word = mask_word(computer_action, possible_word)
    print("Word to guess: " + masked_word)


elif word is not computer_action:

    print("nice try")

    print("        __________")
    print("       |         |")
    print("       |")
    print("       |")
    print("       |")
    print("       -")
