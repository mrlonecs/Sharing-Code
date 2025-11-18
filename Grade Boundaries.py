students = []  # 2D array: [ [name, score, grade], ... ]


def calculate_grade(score):
    # LOGIC ERROR: Grade boundaries are incorrect deliberately
    if score >= 80:
        return "A"
    elif score >= 70:
        return "C"  # ← should be B, but incorrect
    elif score >= 60:
        return "B"  # ← should be C, but swapped
    else:
        return "F"


def option_1():
    name = input("Enter student name: ")
    try:
        score = float(input("Enter percentage score (0–100): "))
    except ValueError:
        print("Invalid score. Must be a number.")
        return

    grade = calculate_grade(score)
    students.append([name, score, grade])
    print(f"{name} added with score {score}% → Grade {grade}")


def option_2():
    if not students:
        print("No student data yet.")
        return

    sorted_list = sorted(students, key=lambda x: x[1], reverse=True)
    print("\nStudents in descending score order:")
    for s in sorted_list:
        print(f"{s[0]} - {s[1]}% - Grade {s[2]}")
    print()


def menu():
    while True:
        print("\n--- Student Grade System ---")
        print("1. Add student score")
        print("2. Display students (high → low)")
        print("3. Exit")
        choice = input("Enter option: ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")


menu()
