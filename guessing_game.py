import random

def main():
    print("Welcome to the number guessing game!")
    choices = int(input("Pick a number between 1 and 10: "))
    number = random.randint(1, 10)
    result(choices, number)

def result(choices, number):
    while True:
        if choices == number:
            print(f"{choices} is equal to {number}")
            print("You won")
            break
        else:
            print(f"{choices} is not equal to {number}")
            print("You lost")

            play_again = input("Do you want to play again? (Y / N): ").upper()
            if play_again != "Y":
                break
                
main()
