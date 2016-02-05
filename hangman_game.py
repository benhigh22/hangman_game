
import random
name = input("Hello there, what's your name? ")

if len(name) > 0 and name.isalpha():
    print (" ")#just for spacing
    print ("Hi, " + name.upper() + " let's play HANGMAN! ")
else:
    print (" ")#just for spacing
    print ("That's a strange name, but who am I to judge?! Let's play HANGMAN!")

print (" ")#just for spacing

random_file = "/usr/share/dict/words"
WORDS = open(random_file).read().splitlines()
random_word = random.choice(WORDS)

counter = 0
guesses = ""
blanks = list("_" * len(random_word))
num_tries = 0
print ("Your secret word has " + str(len(str(random_word))) + " letters in it, shown by the blank spaces below.")
print (" ")#just for spacing
print(blanks)
guessed_letters = []

while num_tries < 8:
    if "_" not in blanks:
        print ("Awesome job, you win!!!")
        break
    print (" ")  #just for spacing
    print ("Pick any letter! ")
    guess = input().lower()

    counter = 0

    for character in random_word:
        if character == guess:
            blanks[counter] = guess
        counter += 1

    if not guess.isalpha():
        print("That is not a letter. Please try again.")
        continue

    elif len(guess) > 1:
        print("That is more than one letter. Please try again.")
        continue

    elif guess in guessed_letters:
        print("You have already guessed that letter. Please try again.")
        continue

    elif guess not in random_word:
        num_tries += 1
        print("Sorry that's wrong. Be careful that was wrong guess number " + str(num_tries) + " out of 8.")
        print (" ")#just for spacing

    elif guess in random_word:
        print ("Great guess!")
        print (" ")
    guessed_letters.append(guess)
    print(blanks)

    if num_tries == 8:
        print (" ")#just for spacing
        print ("Sorry, you lose. Better luck next time!")
        print ("Your secret word was " + random_word)
