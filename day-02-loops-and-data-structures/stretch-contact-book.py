"""
Stretch Exercise: Contact Book Menu
An interactive contact book using a while loop and nested dictionaries.
Each contact stores a name, phone number, and email address.
"""

contacts = {}


def display_menu():
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"No contact found with name '{name}'.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with name '{name}'.")


def display_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    for name, details in contacts.items():
        print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")


def main():
    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_all_contacts()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")


if __name__ == "__main__":
    main()