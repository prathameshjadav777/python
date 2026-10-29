import os
from datetime import datetime


class JournalManager:
    SEPARATOR = "-" * 34

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def _file_exists(self):
        return os.path.exists(self.filename)

    def _create_file_if_missing(self):
        try:
            with open(self.filename, "x", encoding="utf-8"):
                pass
        except FileExistsError:
            pass

    def _read_entries(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if not content:
            return []
        return [block.strip() for block in content.split("\n\n") if block.strip()]

    def add_entry(self):
        text = input("\nEnter your journal entry:\n").strip()
        if not text:
            print("Error: Entry cannot be empty. Please write something.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self._create_file_if_missing()
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n{text}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
        except OSError as error:
            print(f"Error: Could not write to the journal file ({error}).")

    def view_entries(self):
        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return
        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")
            return
        except OSError as error:
            print(f"\nError: Could not read the journal file ({error}).")
            return

        if not entries:
            print("\nNo journal entries found. Start by adding a new entry!")
            return

        print("\nYour Journal Entries:")
        print(self.SEPARATOR)
        for entry in entries:
            print(entry)
            print()

    def search_entries(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()
        if not keyword:
            print("Error: Search term cannot be empty.")
            return

        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return
        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")
            return
        except OSError as error:
            print(f"\nError: Could not read the journal file ({error}).")
            return

        matches = [e for e in entries if keyword.lower() in e.lower()]

        if matches:
            print("\nMatching Entries:")
            print(self.SEPARATOR)
            for entry in matches:
                print(entry)
                print()
        else:
            print(f"\nNo entries were found for the keyword: {keyword}.")

    def delete_entries(self):
        if not self._file_exists():
            print("\nNo journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
        confirm = confirm.strip().lower()

        if confirm == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            except FileNotFoundError:
                print("\nNo journal entries to delete.")
            except PermissionError:
                print("\nError: Permission denied. Cannot delete the journal file.")
            except OSError as error:
                print(f"\nError: Could not delete the journal file ({error}).")
        elif confirm == "no":
            print("\nDeletion cancelled. Your entries are safe.")
        else:
            print("\nInvalid response. Please type 'yes' or 'no'. Deletion cancelled.")

    @staticmethod
    def show_menu():
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

    def run(self):
        actions = {
            "1": self.add_entry,
            "2": self.view_entries,
            "3": self.search_entries,
            "4": self.delete_entries,
        }

        while True:
            self.show_menu()
            try:
                choice = input("\nUser Input:\n").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\nThank you for using Personal Journal Manager. Goodbye!")
                break

            if choice == "5":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("\nInvalid option. Please select a valid option from the menu.")


def main():
    JournalManager("journal.txt").run()


if __name__ == "__main__":
    main()
