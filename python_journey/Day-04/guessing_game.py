secret_num = 42
guess = int(input("Guess the number: "))
while guess != secret_num:
    if guess != secret_num:
        print("not correct, try again.")
        guess = int(input("Guess the number: "))
        if guess == secret_num:
            print("Congratulations! You guessed the correct number.")