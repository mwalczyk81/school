# Assignment 9
# Written by Matthew Walczyk 
# 2/11/2024

# Main function
def main():

    # Get first and last name from the user
    first_name = input("Please enter the student's first name: ")
    last_name = input("Please enter the student's last name: ")

    #Create the student object
    student_object = student(first_name, last_name)


    quit = "1"

    #Loop until user is finished
    while quit == "1":
        grade = input("Please enter the student's grade: ").upper()
        credits = input("Please enter the number of credits: ")

        student_object.calculateGPA(grade, int(credits))

        quit = input("Press 1 to continue entering grades or 2 to quit: ")

    #Display GPA
    student_object.getGPA()



class student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_points = 0
        self.credits = 0
        self.gpa = 0

    def calculateGPA(self, grade, credits):
        self.credits = self.credits + int(credits) 

        #Switch statement for determining grade points
        match grade:
            case "A":
                self.grade_points = self.grade_points + (int(credits) * 4)
            case "B":
                self.grade_points = self.grade_points + (int(credits) * 3)
            case "C":
                self.grade_points = self.grade_points + (int(credits) * 2)
            case "D":
                self.grade_points = self.grade_points + (int(credits) * 1)
            case _:
                self.grade_points = self.grade_points + (int(credits) * 0)

        # Calculate GPA
        self.gpa = self.grade_points / self.credits

    #Method to print GPA
    def getGPA(self):
        print(f"The GPA for {self.first_name} is {round(self.gpa, 1)}")

# Call main function
main()