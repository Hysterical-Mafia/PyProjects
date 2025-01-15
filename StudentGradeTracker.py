#Student Grade Tracker, adds a students name and their final grade at that moment

students_info = []

#while loop to make sure user enters a number greater than 0
while True:
    count = int(input("How many students and grades would you like to add? "))
    if count > 0:
        break
#if loop condition is fulfilled, break and run the for _ loop
for _ in range(count):
    #creates variables for the name and grade being input
    name = input("Student Name: ")
    grade = int(input("Final Grade: "))
    #creates a dictionary to append to the list using the values the user gives
    new_student = {"name": name, "grade": grade}    
    students_info.append(new_student)

#outputs the user information in a clean way, for each student in the students_info list, print their name and final grade like so ("Student Name: Unknown, Final Grade: 100")
for student in students_info:
    print(f"Student Name: {new_student['name']}, Final Grade: {new_student['grade']}")
