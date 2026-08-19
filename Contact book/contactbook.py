# Contact Book

contacts = []


def add_contact():
    print("\n--- Add Contact ---")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("Contact added successfully!")


def view_contacts():
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


def search_contact():
    print("\n--- Search Contact ---")

    name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])

            found = True
            break

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")

    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            print("\nContact found.")

            contact["phone"] = input(
                "Enter new phone number: "
            )

            contact["email"] = input(
                "Enter new email: "
            )

            contact["address"] = input(
                "Enter new address: "
            )

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")

    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():

    while True:

        print("\n==============================")
        print("        CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
