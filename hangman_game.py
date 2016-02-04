
import random
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman! You are allowed up to 8 wrong guesses.")

random_file = "/usr/share/dict/words"
WORDS = open(random_file).read().splitlines()
random_word = random.choice(WORDS)
counter = 0
guesses = ""
blanks = list("_" * len(random_word))
num_tries = 0
print(blanks)

while num_tries < 8:
    if "_" not in blanks:
        print ("You win!")
        break

    guess = input("Choose a letter? ")
    counter = 0
    for character in random_word:
        if character == guess:
            blanks[counter] = guess
        counter += 1

    if guess not in random_word:
        num_tries += 1
        print("Wrong, guess again! " + "Failed attempt number " + str(num_tries))
    print(blanks)
print("Sorry, you lose!")