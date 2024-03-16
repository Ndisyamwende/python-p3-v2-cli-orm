
from helpers import (
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees
)


def main():
    while True:
        print("\nPlease select an option:")
        print("0. Exit the program")
        print("1. List all departments")
        print("2. Find department by name")
        print("3. Find department by id")
        print("4. Create department")
        print("5. Update department")
        print("6. Delete department")
        print("7. List all employees")
        print("8. Find employee by name")
        print("9. Find employee by id")
        print("10. Create employee")
        print("11. Update employee")
        print("12. Delete employee")
        print("13. List all employees in a department")

        choice = input("> ")

        if choice == "0":
            print("Exiting the program.")
            sys.exit()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            name = input("Enter the department's name: ")
            find_department_by_name(name)
        elif choice == "3":
            department_id = int(input("Enter the department's ID: "))
            find_department_by_id(department_id)
        elif choice == "4":
            name = input("Enter the department's name: ")
            create_department(name)
        elif choice == "5":
            department_id = int(input("Enter the department's ID: "))
            name = input("Enter the new department's name: ")
            update_department(department_id, name)
        elif choice == "6":
            department_id = int(input("Enter the department's ID: "))
            delete_department(department_id)
        elif choice == "7":
            list_employees()
        elif choice == "8":
            name = input("Enter the employee's name: ")
            find_employee_by_name(name)
        elif choice == "9":
            employee_id = int(input("Enter the employee's ID: "))
            find_employee_by_id(employee_id)
        elif choice == "10":
            name = input("Enter the employee's name: ")
            position = input("Enter the employee's position: ")
            department_id = int(input("Enter the employee's department ID: "))
            create_employee(name, position, department_id)
        elif choice == "11":
            employee_id = int(input("Enter the employee's ID: "))
            name = input("Enter the new employee's name: ")
            position = input("Enter the new employee's position: ")
            department_id = int(input("Enter the new employee's department ID: "))
            update_employee(employee_id, name, position, department_id)
        elif choice == "12":
            employee_id = int(input("Enter the employee's ID: "))
            delete_employee(employee_id)
        elif choice == "13":
            department_id = int(input("Enter the department's ID: "))
            list_employees_in_department(department_id)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    