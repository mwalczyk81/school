# Assignment 10
# Written by Matthew Walczyk 
# 2/18/2024

# Main function
def main():

    # Get first and last name from the user
    first_name = input("Please enter the student's first name: ")
    last_name = input("Please enter the student's last name: ")
    student_concentration = input("Please enter the studen concentration area. If the student is undeclared type NA: ")

    #Create the student object
    student_object = declared_studen(first_name, last_name, student_concentration)


    quit = "1"

    #Loop until user is finished
    while quit == "1":
        grade = input("Please enter the student's grade: ").upper()
        credits = input("Please enter the number of credits: ")

        student_object.calculateGPA(grade, int(credits))

        quit = input("Press 1 to continue entering grades or 2 to quit: ")

    #Display GPA
    student_object.getGPA()

    student_year = student_object.getYear()

    print(student_year)



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

class declared_studen(student):
    def __init__(self, first_name, last_name, concentration):
        super().__init__(first_name, last_name)
        self.concentration = concentration.upper()
    
    def getConcentration(self):
        return self.concentration
    
    def getYear(self):
        if self.concentration == "NA":
            return f"{self.first_name} {self.last_name} has not selected a concentration"

        if self.credits <= 33:
            return f"{self.first_name} {self.last_name} Year One Student"
        elif self.credits <= 66:
            return f"{self.first_name} {self.last_name} Year Two Student"
        elif self.credits <= 96:
            return f"{self.first_name} {self.last_name} Year Three Student"
        elif self.credits <= 130:
            return f"{self.first_name} {self.last_name} Year Four Student"
        else:
            return "Multiyear student"
    

# Call main function
main()