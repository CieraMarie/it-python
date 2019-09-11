














guess = -1

while guess != the_number:
    guess_text = input("what is your guess? ")
    guess = int(guess_text)

    if guess> 100 or guess < 0:
        print("please choose a number that is between 0 and 100. ")
        elif guess > the_number:
            print(f"Sorry {name}, but your guess is too HIGH. try again.")
            elif guess < the_number:
                print(f"Sorry {name}, but your guess is too LOW. try again.")
                else:
                    print(f"You guessed it! Congratulations, {name}!")



