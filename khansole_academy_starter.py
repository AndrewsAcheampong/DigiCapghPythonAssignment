"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

count = 0;
active = True;


while active:
    # random_one and random_two are the two random integers generated to form the addition.
    random_one = random.randint(10, 99);
    random_two = random.randint(10,99);

    # Addition on both random numbers is stored in a variable called random_addition
    random_addition = random_one + random_two

    # The user is asked to solve the question generate.
    user_input = int(input("What is " + str(random_one) + " + " + str(random_two) + " ? "));

    # The conditional statements are made here and that's if the input from the user is 
    # not equal to the preffered answer he should be alerted, corrected and retested with different question.
    if user_input != random_addition:
        count = 0
        print("Your answer is " + str(user_input));
        print("Incorrect. The expected number is " + str(random_addition));
    
    # This program runs when the user enters a correct answer and in three rows.
    elif user_input == random_addition:
        count+= 1; 
        print("You've gotten " + str(count) + " correct in a row");
        if (count == 3):
            print("Congratulations, You mastered addition");
            active = False;
        

