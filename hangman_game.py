
import random
name = input("Hello there, what's your name? ")
print (" ")#for spacing

while True:
    if len(name) > 0 and name.isalpha():
        print ("Hi " + name.upper() + " how are you today? ")
        print (" ")#for spacing
        break

    else:
        print ("Sorry, that's not a valid name.")
        name = input("Enter your name. ")
        continue
mood = input('Enter either "good", "bad", or "shut up computer you dont know me" ').lower()
while True:
    if mood == "good":
        print (" ")
        print ("Did we just become best friends? I think we did! ")
        print (" ")#for spacing
        break
    elif mood == "bad":
        print (" ")
        print ("Well, we can still be best friends! ")
        print (" ")#for spacing
        break
    elif mood == "shut up computer you dont know me":
        print (" ")
        print ("Wow, that was rude. We better play HANGMAN to become best friends! ")
        print (" ")#for spacing
        break
    else:
        print ("Sorry, that's not a valid choice ")
        print (" ")#for spacing
        mood = input('Enter either "good", "bad", or "shut up computer you dont know me" ').lower()
        continue
answer = input('Look at all of this space for activities! Want to play HANGMAN? Type "y" or "n". Just dont touch my drumset... EVER! ').lower()
while True:
    if answer == "y":
        print (" ")
        print ("Awesome, let's play! ")
        break
    elif answer == "n":
        print (" ")#for spacing
        print ("Come on, why don't you reconsider... ")
        print (" ")#for spacing
        answer = input("Do you want to play HANGMAN? Type y or n ").lower()
        continue
    else:
        print (" ")#for spacing
        print ("Sorry, you must enter either y or n ")
        answer = input("Do you want to play HANGMAN? Type y or n ").lower()
        continue

random_file = "/usr/share/dict/words"
WORDS = open(random_file).read().splitlines()
random_word = random.choice(WORDS)

counter = 0
blanks = list(("_" * len(random_word)))
num_tries = 0
print (" ")#for spacing
print ("Your secret word has " + str(len(str(random_word))) + " letters in it, shown by the blank spaces below.")
print (" ")#for spacing
print(blanks)
guessed_letters = []
play_again = True
while num_tries < 8:
    if "_" not in blanks:
        print ("Awesome job, you win!!!")
        break
    print (" ")#for spacing
    print ("Pick any letter! ")
    guess = input().lower()
    other_guess = str(list(guess))
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
        print (" ")#for spacing
        print("     LETTER(S) ALREADY GUESSED: " + str(str(guessed_letters) + " LAST LETTER GUESSED: " + other_guess))
        print (" ")#for spacing

    elif guess in random_word:
        print ("Great guess!")
        print (" ")#for spacing
        print("     LETTER(S) ALREADY GUESSED: " + str(str(guessed_letters) + " LAST LETTER GUESSED: " + other_guess))
        print (" ")#for spacing

    guessed_letters.append(guess)
    print(blanks)

    if num_tries == 8:
        print (" ")#for spacing
        print ("Sorry, you lose. We can still be best friends, right?")
        print (" ")#for spacing
        print ("Your secret word was " + random_word.upper())



