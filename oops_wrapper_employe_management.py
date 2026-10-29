class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __del__(self):
        pass


class Employee(Person):
    def __init__(self, name="Unknown", age=0, employee_id="N/A", salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = float(salary)

    @classmethod
    def from_string(cls, data, sep=","):
        name, age, emp_id, salary = [x.strip() for x in data.split(sep)]
        return cls(name, int(age), emp_id, float(salary))

    @classmethod
    def from_person(cls, person, employee_id, salary):
        return cls(person.name, person.age, employee_id, salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = float(salary)

    def display(self):
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ${self.get_salary()}")

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name="Unknown", age=0, employee_id="N/A",
                 salary=0.0, department="N/A"):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name="Unknown", age=0, employee_id="N/A",
                 salary=0.0, programming_language="N/A"):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


MENU = """
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
"""


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def create_person(store):
    name = input("Enter Name: ")
    age = read_int("Enter Age: ")
    store["person"] = Person(name, age)
    print(f"\nPerson created with name: {name} and age: {age}.")


def create_employee(store):
    name = input("Enter Name: ")
    age = read_int("Enter Age: ")
    emp_id = input("Enter Employee ID: ")
    salary = read_float("Enter Salary: ")
    emp = Employee(name, age, emp_id, salary)
    store["employee"] = emp
    print(f"\nEmployee created with name: {name}, age: {age}, "
          f"ID: {emp_id}, and salary: ${emp.get_salary()}.")


def create_manager(store):
    name = input("Enter Name: ")
    age = read_int("Enter Age: ")
    emp_id = input("Enter Employee ID: ")
    salary = read_float("Enter Salary: ")
    dept = input("Enter Department: ")
    mgr = Manager(name, age, emp_id, salary, dept)
    store["manager"] = mgr
    print(f"\nManager created with name: {name}, age: {age}, "
          f"ID: {emp_id}, salary: ${mgr.get_salary()}, "
          f"and department: {dept}.")


def show_details(store):
    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    choice = read_int("Enter your choice: ")

    mapping = {1: ("person", "Person"),
               2: ("employee", "Employee"),
               3: ("manager", "Manager")}

    if choice not in mapping:
        print("\nInvalid choice.")
        return

    key, label = mapping[choice]
    obj = store.get(key)
    if obj is None:
        print(f"\nNo {label} has been created yet.")
        return

    print(f"\n{label} Details:")
    obj.display()

    if key in ("employee", "manager"):
        print(f"Is subclass of Employee? "
              f"{issubclass(type(obj), Employee)}")


def main():
    store = {}
    actions = {1: create_person, 2: create_employee,
               3: create_manager, 4: show_details}

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        print(MENU)
        choice = read_int("Enter your choice: ")
        print()

        if choice == 5:
            store.clear()
            print("Exiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break
        elif choice in actions:
            actions[choice](store)
            print("\n--- Choose another operation ---")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
