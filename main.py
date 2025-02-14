
# TASK: Write a function that returns a random encouragement message.

# Import the random module

# Define a function with no parameters that returns a string

# Create four different message variables

# Generate a random number from 1 to 4
import random

def message_one():
    print("you got the first message")

def message_two():
    print("you got the second message")

def message_three():
    print("you got the third message")

def message_four():
    print("you got the fourth message")

    functions = [message_one, message_two, message_three, message_four]

    random.choice(functions)()
# Use if-elif statements to return the corresponding message
selected_function = random.choice(functions)
message = selected_function() 

print(message)
# Call the function and print the result