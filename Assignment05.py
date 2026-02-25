# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Marina Osiechko, 02/21/2026, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = 'Enrollments.json'

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name# one row of student data dictionary (which is one row) of a course entered by the user.
student_data: dict = {}
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

'''# Formatting names to add to the newly created dictionary
student_row1: dict[str, str] = {"FirstName": "Bob", "LastName": "Smith", "CourseName": "Python 100"}
student_row2: dict[str, str] = {"FirstName": "Sue", "LastName": "Jones", "CourseName": "Python 100"}
students: list[dict[str, str]] = [student_row1, student_row2]

# Create the file (or overwrite if exists), commenting this out to avoid overwriting data 
file = open('Enrollments.json', 'w')
json.dump(students, file, indent=2)  # Write the Python data into the file as JSON
file.close()
print('Data Saved!')'''

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
try:
    # Open JSON file, dump data into students table and closes (load converts JSON into Python)
    file = open(FILE_NAME, 'r')
    students = json.load(file)  # use load with 'r'

except FileNotFoundError as e:
    print('Test file must exist before running this script!\n')
    print('-- Technical Error Message --')
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:  # this is general Catch All error exception
    print('There was a non-specific error!\n')
    print('-- Technical Error Message --')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input('What would you like to do: ')

    # Input user data
    if menu_choice == '1':  # This will not work if it is an integer!
        try:
            student_first_name = input('Enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('The first name should not contain numbers.')

            student_last_name = input('Enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('The last name should not contain numbers.')

            course_name = input('Please enter the name of the course: ')

            # Collected data is added to a dictionary named student_data
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            # Student_data is added to the students 2D list of dictionary rows
            students.append(student_data)
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        except ValueError as e:
            print(e)  # Print the custom message
            print('-- Technical Error Message --')
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print('There was a non-specific error!\n')
            print('-- Technical Error Message --')
            print(e, e.__doc__, type(e), sep='\n')
        continue  # the loop

    # Present the current data
    elif menu_choice == '2':
        # Process the data to create and display a custom message
        print("-" * 50)
        for student_data in students:
            print(f'{student_data["FirstName"]},{student_data["LastName"]},{student_data["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == '3':
        # Load student data into JSON (list of dictionaries) table (dump changes Python to JSON)
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file, indent=2)
        except TypeError as e:
            print('Please check that the data is a valid JSON format\n')
            print('-- Technical Error Message --')
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('-- Technical Error Message --')
            print('Built-In Python error info: ')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()

        print('The following data was saved to file!')
        for student in students:
            print(
                f'Student {student["FirstName"]} {student["LastName"]} is enrolled in '
                f'{student["CourseName"]}'
            )
        continue  # the loop

    # Stop the loop
    elif menu_choice == '4':
        break  # out of the loop
    else:
        print('Please only choose option 1, 2, 3, or 4')

print('Program Ended')
