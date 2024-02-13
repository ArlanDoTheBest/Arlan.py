import random

def guessing():
    random_number = random.randint(1, 20)
    print("Hello! What is your name?\n")
    name = str(input())
    print("Well,", name, "I am thinking of a number between 1 and 20.\n")
    i = 1
    while(True):
        print("Take a guess.\n")
        number = int(input())
        if(number != random_number):
            print("Your guess is too low.\n")
            i+=1
            continue
        elif(number == random_number):
            print("Good job,",name,"! You guessed my number in ," ,i, "guesses!")
            
guessing()
        
