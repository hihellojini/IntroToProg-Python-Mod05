# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And JSON Files
# Desc: Shows how work with dictionaries and json files when using a table of data
# Change Log: (Who, When, What)
#   JDuldulao,05/14/2025,Created Script
# ------------------------------------------------------------------------------------------ #
import json
import io as _io  # Needed to try closing in the finally block

# Define the Data Constants
FILE_NAME: str = 'Enrollments.json'

MENU: str = '''
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

#Define data variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  ## Holds the course name of the student entered by the user.
file = _io.TextIOWrapper  # This is the actual type of the file handler
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
message: str = ''  # Holds a custom message string
file_data: str = ''  # Holds combined string data separated by a comma.

# When the program starts, read the file data into a list (students)
# Extract the data from the file
# Use of try-except error handling
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("\nText file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Repeat the follow tasks
while (True):

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()

    if menu_choice == "1":
        try:
            # Input the data
            student_first_name = input("Enter the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Enter the student's course name? ")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            continue

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            message = " {},{},{}."
            print(message.format(student["FirstName"], student["LastName"], student["CourseName"]))
        print("-"*50)
        continue

    elif menu_choice == "3":
        try:
            #  Save the data to the file
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()

            print("-" * 50)
            print("The following data has been saved to the file:")
            for student in students:
                message = " {},{},{}."
                print(message.format(student["FirstName"], student["LastName"], student["CourseName"]))
            print("-" * 50)
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    elif menu_choice == "4":
        break  # out of the while loop

    else:
        continue
