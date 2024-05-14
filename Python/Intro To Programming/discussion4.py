# Assignment 4 - Program to convert miles into kilometers
# Input - Integer for the amount of miles driven
# Output - Float for the number kilometers driven 1 mile = 1.60934 kilometer
# Written by Matthew Walczyk 
# 1/3/2024

# Main function
def main():

    # Display the intro
    intro()

    try:
        # Get the number of miles
        miles_driven = int(input("Enter the number of miles:"))

        miles_to_kilometers(miles_driven)

    # Catch errors and try again
    except:
        print("Invalid input. Please enter only a number")
        print()
        main()


# Intro function to display an introductory screen
def intro():
    print("This program converts measurements in miles to kilometers")
    print("For your reference the formula is 1 gallon = 1.60934 kilometers")
    print()

# Accepts the number of miles and displays the equivalent kilometers
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    print(f"That converts to {kilometers} kilometers")

# Call main function
main()