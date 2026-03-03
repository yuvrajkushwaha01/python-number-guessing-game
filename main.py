#import random module
import random

print("Select Your Difficulty Level:")
print("1.Easy Level You have (10 attempts) to guess:")
print("2.Medium Level You have (8 attempts) to guess:")
print("3.Hard Level You have (6 attempts) to guess:")
#asking user choice
choice=input("Choose Your Difficulty Level (1/2/3):")


#set attempt based on user difficulty level choosen
if choice == "1":
    attempts=10
elif choice == '2':
    attempts=8
else:
    attempts=6

#generate random number using random module
num= random.randint(1,101)
print("You have",attempts," attempts To guess the number:")

#start guessing number using while loop
while attempts > 0:
 guess = int(input("Enter Your Guess (1 - 100):"))
 if guess == num:
    print(" Congrulation Correct Guess ! You Win the Game")
    break
 elif guess > num:
    print("Too High! Try Lower number:")
 else:
    print("Too Low! Try Higher number:")

    attempts -= 1
    print("You have remaining Attempts to guess:" , attempts)
     
# if user not guess correct number in given attempts
if attempts == 0 and guess != num:
   print("Game Over!")
   print(" The Correct number was", num)
