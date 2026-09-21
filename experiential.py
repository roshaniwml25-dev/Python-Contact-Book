import json

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- ALL CONTACTS -----")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name  :", contact["name"])
        print("Phone :", contact["phone"])
        print("Email :", contact["email"])


# Search contact
def search_contact(contacts):
    search = input("Enter name or phone number to search: ")

    found = False

    for contact in contacts:
        if (search.lower() in contact["name"].lower()
                or search in contact["phone"]):

            print("\nContact Found!")
            print("Name  :", contact["name"])
            print("Phone :", contact["phone"])
            print("Email :", contact["email"])

            found = True

    if not found:
        print("Contact not found.")


# Edit contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            print("\nCurrent Details:")
            print("Name  :", contact["name"])
            print("Phone :", contact["phone"])
            print("Email :", contact["email"])

            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")

            save_contacts(contacts)

            print("Contact updated successfully!")
            return

    print("Contact not found.")


# Delete contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contacts.remove(contact)
            save_contacts(contacts)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n==============================")
        print("        CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please try again.")


main()