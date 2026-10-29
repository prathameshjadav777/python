# 

## 📌 Project Overview

The **Employee Management System** is a menu-driven Python project that demonstrates Object-Oriented Programming (OOP). It allows users to create and view details for people, employees, and managers through a simple console interface.

The project uses classes, inheritance, encapsulation, class methods, and method overriding to organize employee information and demonstrate relationships between different types of people in an organization.

## ✨ Features

- **Create a Person:** Store a person's name and age.
- **Create an Employee:** Store personal details, employee ID, and salary.
- **Create a Manager:** Store employee details along with a department.
- **View Details:** Display the saved details of a Person, Employee, or Manager.
- **Input Validation:** Handle invalid integer and numeric input with helpful messages.
- **Salary Validation:** Prevent a negative salary when using the salary setter.
- **Menu-Driven Interface:** Choose operations from a numbered console menu.
- **Object-Oriented Design:** Organize data and behavior using reusable classes and methods.

## 🧠 OOP Concepts Used

- **Classes and Objects:** `Person`, `Employee`, `Manager`, and `Developer` define different object types.
- **Inheritance:** `Employee` inherits from `Person`; `Manager` and `Developer` inherit from `Employee`.
- **Encapsulation:** Employee ID and salary are stored in private attributes in the `Employee` class and accessed through getter and setter methods.
- **Polymorphism / Method Overriding:** The `display()` method is customized in the employee-related classes to show their specific details.
- **Constructor (`__init__`):** Initializes object attributes.
- **Class Methods:** `from_string()` and `from_person()` provide alternative ways to create an employee.
- **`super()`:** Reuses initialization and display behavior from parent classes.
- **Exception Handling:** `try` and `except` help handle invalid numeric input.

## 🧩 Main Classes

| Class | Purpose |
|---|---|
| `Person` | Stores and displays a person's name and age. |
| `Employee` | Extends `Person` with an employee ID and salary. |
| `Manager` | Extends `Employee` with a department. |
| `Developer` | Extends `Employee` with a programming language. |

## ⚙️ Main Functions

- `read_int()` — repeatedly asks for input until a valid whole number is entered.
- `read_float()` — repeatedly asks for input until a valid numeric value is entered.
- `create_person()` — creates and stores a Person object.
- `create_employee()` — creates and stores an Employee object.
- `create_manager()` — creates and stores a Manager object.
- `show_details()` — displays details for a selected stored object.
- `main()` — runs the menu and directs the selected operation.

## 🗂️ How the Project Works

1. The program displays a menu of available operations.
2. The user selects whether to create a Person, Employee, or Manager, view details, or exit.
3. The program requests the relevant information and creates an object.
4. Created objects are kept in a dictionary while the program runs.
5. The user can choose to display the details of an object that has already been created.
6. Choosing Exit clears the stored dictionary and ends the program.

## 🛠️ Technologies Used

- **Language:** Python
- **Concepts:** Object-Oriented Programming, inheritance, encapsulation, polymorphism, and exception handling
- **Interface:** Command-line / console

## 🎯 Learning Objectives

This project helps demonstrate how Python OOP concepts can be used to model people and employee roles, reuse code through inheritance, validate user input, and organize a menu-driven application.

## 📷 Screenshots
<img width="853" height="852" alt="Screenshot 2026-10-29 125820" src="https://github.com/user-attachments/assets/f6b14dcb-3b73-48d9-a980-c43d7abd3daf" />
<img width="1075" height="876" alt="Screenshot 2026-10-29 125851" src="https://github.com/user-attachments/assets/cf488817-2b61-4da0-a9fd-bafeb7deaa17" />
<img width="558" height="126" alt="Screenshot 2026-10-29 125906" src="https://github.com/user-attachments/assets/24c76a93-5e61-49d3-b062-545e0a1d22eb" />



## 🎥 Demo Video


https://github.com/user-attachments/assets/5e5e9ef2-d91f-4009-856f-1c42dd637616






