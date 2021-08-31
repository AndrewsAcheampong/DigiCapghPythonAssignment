"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
random_number = random.randint(30, 50); 

# This p
prompt =" I am thinking of a number between 1 and 99";
print(prompt);
active = True;


while active:
    message = int(input("Enter a guess: "));
    
    if (message < random_number):
        print("Your guess is too low");

    elif (message > random_number):
        print("Your guess is too high");
         
    elif message == random_number:
        print("Congrats! The number was : " + message);
        active = false;
