"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        value = int(input("Enter a number :"))
        # when user input number is integer, while loop will stop
        finished = True
    except ValueError: #Filter user input number is integer or not
        print("Please enter a valid integer.")
print("Valid result is:", value)
