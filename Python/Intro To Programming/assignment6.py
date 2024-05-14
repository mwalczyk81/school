# Assignment 6 
# Written by Matthew Walczyk 
# 1/21/2024

import statistics
# Main function
def main():
    numbers = []

    for i in range(20):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print(f"The lowest number is {min(numbers)}")

    print(f"The highest number is {max(numbers)}")

    print(f"The total is {sum(numbers)}")

    print(f"The average of the numbers is {statistics.mean(numbers)}")

# Call main function
main()