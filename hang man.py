import random

word_bank = ["GLASS", "COMPUTER", "JAVA", "APPLE", "CHAIR", "FISH", "oslab", "IPHONE", "TRAIN"]
word = random.choice(word_bank)


joon = 7

user_true_chars = []

while True:
    IS_WIN = True
    for char in word:
        if char in user_true_chars:
            print(char, end="")
        else:
            print("-", end="")
            IS_WIN = False

    if IS_WIN:
        print("\n\n YOU WON THE GAME.")
        break

    user_char = input("\n ENTER THE CHARACTER YOU GUESSED: ")

    if user_char in word:
        print("✔")
        user_true_chars.append(user_char)
    else:
        joon -= 1
        print("❌")
    if joon == 0:
        print("\n SORRY GAME OVER.")
        break