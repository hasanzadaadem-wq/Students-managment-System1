from database import *



def menu():
    print("""
====================================
       STUDENT MANAGEMENT SYSTEM
====================================

1. Add Student
2. Show Students
3. Update Student
4. Delete Student
5. Search Student

0. Exit

""")


def main():
    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                show_students()

            elif choice == 3:
                update_student()

            elif choice == 4:
                delete_student()

            elif choice == 5:
                search_student()

            elif choice == 0:
                print("Program closed.")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()