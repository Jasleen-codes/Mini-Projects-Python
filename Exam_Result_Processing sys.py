# Exam_result_processing system
#
# List to maintain student records
students = []
# Dictionary to store marks
student_marks = {}

# Calculation Functions 
def calculate_total(marks):
    return sum(marks.values())

def calculate_percentage(marks):
    return calculate_total(marks) / len(marks)

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

#  Add Student
def add_student():
    try:
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        # Student details stored as tuple
        student = (roll_no, name)

        marks = {
            "Maths": int(input("Enter Maths Marks: ")),
            "Science": int(input("Enter Science Marks: ")),
            "English": int(input("Enter English Marks: "))
        }

        for mark in marks.values():
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")

        students.append(student)
        student_marks[roll_no] = marks

        print("Student record added successfully!")

    except ValueError as e:
        print("Error:", e)

# Grade Report 
def generate_grade_report():
    if not students:
        print("No records found!")
        return

    with open("results.txt", "w") as file:

        print("\n-- GRADE REPORT --")

        for student in students:
            roll_no, name = student

            marks = student_marks[roll_no]
            total = calculate_total(marks)
            percentage = calculate_percentage(marks)
            grade = calculate_grade(percentage)

            print("\nRoll No:", roll_no)
            print("Name:", name)
            print("Total:", total)
            print("Percentage:", round(percentage, 2))
            print("Grade:", grade)

            file.write(
                f"{roll_no}, {name}, {total}, "
                f"{percentage:.2f}, {grade}\n"
            )

        print("\nResults saved to results.txt")

# Rank List 
def generate_rank_list():

    rank_list = []

    for student in students:
        roll_no, name = student
        total = calculate_total(student_marks[roll_no])

        rank_list.append((total, roll_no, name))

    rank_list.sort(reverse=True)

    print("\n--- RANK LIST---")

    rank = 1
    for total, roll_no, name in rank_list:
        print(f"Rank {rank}: {name} ({roll_no}) - {total} Marks")
        rank += 1

# Main Menu 
while True:

    print("\n-- EXAM RESULT PROCESSING SYSTEM ---")
    print("1. Add Student")
    print("2. Generate Grade Report")
    print("3. Generate Rank List")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        generate_grade_report()

    elif choice == "3":
        generate_rank_list()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")