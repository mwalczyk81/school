# Assignment 6 - Program to convert miles into kilometers
# Input - string for file name, name, address, phone number
# Output - file name, name, address, phone number
# Written by Matthew Walczyk 
# 1/13/2024

import csv
# Main function
def main():

    try:
        file_name = input("Enter the file name: ")

        name = input("Enter your name: ")

        address = input("Enter your address: ")

        phone_number = input("Enter your phone number: ")

        create_file(file_name, name, address, phone_number)

        print(f"Here is what you entered: ")

        read_file(file_name)

    # Catch errors and try again
    except:
        print("An error occurred. Please try again.")
        print()
        main()


def create_file(file_name, name, address, phone_number):
    #Put data into a list
    row = [[name, address, phone_number]]
    #Open file
    with open(f"{file_name}.csv", 'w') as csvfile:
        #Create the writer
        csvwriter = csv.writer(csvfile)
        #Write the data to the file
        csvwriter.writerow(row)


def read_file(file_name):
    #Open the file
    with open(f"{file_name}.csv", 'r') as csvfile:
        #Read the contents
        read = csv.reader(csvfile)
        #Loop and print everything
        for lines in read:
            print(lines)
        

# Call main function
main()