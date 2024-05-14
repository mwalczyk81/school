# Assignment 3 - Program to calcuate the cost of installing fiber optice cable
# Input - Integer for the amount of interest, integer for amount of investment
# Output - Float for the total investment, integer for the year number
# Written by Matthew Walczyk 
# 12/15/2023

# Capture the initial investment
while True:
    try:
        # Cast the value to an integer and if successful exit the loop
        initial_investment = int(input("Please enter your initial investment. Note enter a whole number (ex 10000): "))
        break
    except ValueError:
        # Give the user an error message asking for an integer and execute the loop again
        print("Please enter a whole number.")

# Capture the interest rate
while True:
    try:
        # Cast the value to an integer and if successful exit the loop then divide by 100 to get the percent
        interest = int(input("Please enter your interest rate. Note enter a whole number (ex 10000): ")) / 100
        break
    except ValueError:
        # Give the user an error message asking for an integer and execute the loop again
        print("Please enter a whole number.")

# Set values to be updated in the loop
total_investment = initial_investment
year = 1

# Set the loop to go until the total amount is no longer less than the initial amount times 2
while total_investment < initial_investment * 2:
    # Determine the amount gained in this iteration
    interest_gained = total_investment * interest
    # Update the total with the gained amount
    total_investment += interest_gained
    # Print out the message to the user
    print(f"Year Number: {year} Investment Amount: {total_investment}")
    #Increment the year
    year += 1