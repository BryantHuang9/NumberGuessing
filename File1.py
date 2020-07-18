import random

def compare_num(num, answer, tries):
    if tries > 0:
        if int(num) == answer:
            print("Correct. Congratulations!")
            exit()
        elif answer == 1:
            print("Hint: It is a prime number.")
        elif answer == 2:
            print("Hint: It is a multiple of 2.")
        elif answer == 3:
            print("Hint: It is a multiple of 3.")
        elif answer == 4:
            print("Hint: It is a perfect square.")
        elif answer == 5:
            print("Hint: It is a multiple of 5.")
        elif answer == 6:
            print("Hint: It is a multiple of 2.")
        elif answer == 7:
            print("Hint: It is a prime number.")
        elif answer == 8:
            print("Hint: It is a multiple of 4.")
        elif answer == 9:
            print("Hint: It is a perfect square.")
        elif answer == 10:
            print("Hint: It is a multiple of 5.")
        if tries == 2:
            print("You have " + str(tries) + " more tries.")
        if tries == 1:
            print("You have " + str(tries) + " more try.")
    elif tries == 0:
        if int(num) == answer:
            print("Correct. Congratulations!")
        else:
            print("Game over.")
            print("The number is " + str(answer))


print("Welcome to the Number Guessing Game! You will have 3 tries to guess the right number. Good luck!")
answer = random.randint(1, 10)
# print(answer)
tries = 3
attempt = 1
while tries <= 3 and tries > 0:
    tries -= 1
    num = input("Attempt # " + str(attempt) + " Guess an integer between 1 and 10: ")
    attempt += 1
    compare_num(num, answer, tries)





