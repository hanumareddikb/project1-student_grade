word1 = input("Enter the word for game: ")
lives = len(word1*2)

word = list(word1.lower())

while lives > 0:
    a = input("Enter a letter: ")

    if a in word:
        print("Your guess is right, Try next letter")
        lives -= 1
        word.remove(a)

        if len(word)==0:
            print(f"Hey... You won the game!! and the word is {word1}")
            break

    else:
        print("Oops your guess is not correct, Try again")
        lives -= 1

        if lives < len(word):
            print(f"You are out of lives, so you lost the game and the word is {word1}")
            break
