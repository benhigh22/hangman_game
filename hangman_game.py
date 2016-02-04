
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman! You are allowed up to 8 wrong guesses.")

random = "bathroom"
counter = 0
guesses = ""
blanks = list("_" * len(random))
num_tries = 0
print(blanks)

while num_tries < 8:
    guess = input("Choose a letter? ")
    counter = 0
    for character in random:
        if character == guess:
            blanks[counter] = guess
            print(counter)
        counter += 1

    else:
        print(blanks)

    if guess not in random:
        num_tries += 1
        print ("Wrong, guess again! " + "Failed attempt number " + str(num_tries))