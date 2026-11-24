import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(name, age, grade):
    students = load_students()

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def show_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


def update_student(student_id, name, age, grade):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            student["name"] = name
            student["age"] = age
            student["grade"] = grade

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(student_id):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def search_student(name):
    students = load_students()

    for student in students:
        if name.lower() in student["name"].lower():
            print(student)
            return

    print("Student not found.")