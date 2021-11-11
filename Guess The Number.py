#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty: easy or hard\n").lower()
if difficulty=='easy':
  number_of_attempts=10
  computer_guess=random.randint(1,100)
  while number_of_attempts>0:
    user_guess=int(input("Make a guess: "))
    if user_guess>computer_guess:
      print("Too high. Guess again")
      number_of_attempts-=1
      print("You have {} number of attempts left".format(number_of_attempts))
      if number_of_attempts==0:
        print("YOU LOST.")
    elif user_guess==computer_guess:
      print("You got it.The number was {}.".format(computer_guess))
      break
    else:
      print("Too low. Guess again")
      number_of_attempts-=1
      print("You have {} number of attempts left".format(number_of_attempts))
      if number_of_attempts==0:
        print("YOU LOST.")
      
elif difficulty=='hard':
  number_of_attempts=5
  computer_guess=random.randint(1,100)
  while number_of_attempts>0:
    user_guess=int(input("Make a guess: "))
    if user_guess>computer_guess:
      print("Too high. Guess again.")
      number_of_attempts-=1
      print("You have {} number of attempts left".format(number_of_attempts))
      if number_of_attempts==0:
        print("YOU LOST.")
    elif user_guess==computer_guess:
      print("You got it.The number was {}.".format(computer_guess))
      break
    else:
      print("Too low. Guess again")
      number_of_attempts-=1
      print("You have {} number of attempts left".format(number_of_attempts))
      if number_of_attempts==0:
        print("YOU LOST.")
else:
  print("Wrong input")
 


