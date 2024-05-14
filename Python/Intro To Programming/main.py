# Assignment 2 - Program to calcuate the cost of installing fiber optice cable
# Input - Integer for the amount of feet needed
# Output - Float for the total price which is feet multiplied by .87
# Written by Matthew Walczyk 
# 12/4/2023

# Welcome message
print("Welcome to cost calculation program")

# Capture the number of feet of cable from the user while making sure they enter an integer
while True:
    try:
        # Cast the value to an integer and if successful exit the loop and print the cost
        feet_of_cable = int(input("Please enter the number of feet of cable you need: "))
        break
    except ValueError:
        # Give the user an error message asking for an integer and execute the loop again
        print("Please enter" + "an integer.")

# Set the standard price
price = .87

for item in "Hi":
    print("hi!")

# Check to see if order qualifies for discount and update the price if it does
if(feet_of_cable > 100):
    price = .8
elif(feet_of_cable > 250):
    price = .7
elif(feet_of_cable > 500):
    price = .5

# Print the cost (feet multiplied by price) to the user and the company name
print(f"The cost is ${feet_of_cable * price}...Thank you for choosing My Fiber Optics Inc.")