# 📔 Personal Journal Manager

## 📌 About the Project

**Personal Journal Manager** is a menu-driven Python application for keeping personal journal entries in a text file. It allows users to add entries, view saved entries, search by keyword or date, and delete all entries after confirmation.

Each entry is saved with an automatic date and time.

## ✨ Features

- ✍️ **Add a Journal Entry** — Save a new entry with a timestamp.
- 📖 **View All Entries** — Display previously saved entries.
- 🔎 **Search Entries** — Find entries by keyword or date.
- 🗑️ **Delete All Entries** — Delete saved entries after confirmation.
- 💾 **File-Based Storage** — Save entries in `journal.txt`.
- ✅ **Input Validation** — Reject empty entries and empty search terms.
- 🛡️ **Error Handling** — Handle common file access errors and invalid menu choices.

## 🖼️ Project Screenshot
<img width="521" height="845" alt="Screenshot 2026-10-29 173432" src="https://github.com/user-attachments/assets/8729beec-d539-4df4-a34f-27f938c981cc" />
<img width="652" height="901" alt="Screenshot 2026-10-29 173507" src="https://github.com/user-attachments/assets/f6b8cdab-db98-45f3-aa6c-2510a434606d" />
<img width="613" height="285" alt="Screenshot 2026-10-29 173526" src="https://github.com/user-attachments/assets/c12b09e3-1a9e-47b4-bb96-34e5b186a27b" />



*Replace the placeholder with your screenshot URL, or upload the screenshot to your GitHub repository and link to that file.*

## 🎬 Demo Video





*Replace the placeholder with your YouTube or Google Drive demo link.*

## 🛠️ Concepts Used

- Python classes and objects
- Object-oriented programming (OOP)
- File handling and text-file operations
- Exception handling (`try` and `except`)
- Lists and list comprehensions
- String methods and formatting
- Date and time handling with `datetime`
- Dictionaries and menu-driven control flow
- Functions and methods

## ⚙️ How It Works

The program displays a menu and asks the user to choose an action. The selected option calls the matching method in the `JournalManager` class.

Entries are saved in a text file with timestamps. The application reads this file to display or search entries. Before deleting all entries, it asks the user for confirmation.

## 📂 Project Structure

- **`Personal Journal Manager.py`** — Main Python program containing the journal-management functionality.
- **`journal.txt`** — Stores journal entries and is created when a new entry is added, if it does not already exist.

## 🎯 Project Objective

This project demonstrates how Python can be used to build a practical command-line application using object-oriented programming, file handling, input validation, and exception handling.

## 👨‍💻 Conclusion

Personal Journal Manager offers a straightforward way to record and manage personal notes while demonstrating core Python programming concepts.
