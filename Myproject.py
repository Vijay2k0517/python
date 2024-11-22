import random
number_generate = random.randint(1, 100)
attempt_left = 5

print("Welcome to the Random Number Guessing Game!")
print("Let's see if we got matching numbers. If you guess the number, you win!")
print("NOTE: You have only 5 attempts!")

while attempt_left > 0:
    try:
        guess = int(input("Guess the number: "))
        print(f"Attempts Left: {attempt_left - 1}")

        if guess == number_generate:
            print("Hoorayyy! You got it right 🎉")
            break  
        elif guess < number_generate:
            print("Too low! Try again :)")
        else:
            print("Too high! Try again :)")

        attempt_left -= 1

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if attempt_left == 0:
    print(f"Sorry, you are out of attempts. The number was {number_generate}. \nBetter luck next time! :)")
