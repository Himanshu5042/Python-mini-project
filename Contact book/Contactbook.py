# ==========================================
#          CONTACT BOOK
# ==========================================

contacts = []


# Function to add a contact
def add_contact():
    print("\n---------- ADD CONTACT ----------")

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

    print("\nContact added successfully!")


# Function to view all contacts
def view_contacts():
    print("\n---------- ALL CONTACTS ----------")

    if len(contacts) == 0:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name    :", contact["name"])
        print("Phone   :", contact["phone"])
        print("Email   :", contact["email"])
        print("Address :", contact["address"])


# Function to search a contact
def search_contact():
    print("\n---------- SEARCH CONTACT ----------")

    name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            print("\nContact Found!")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True
            break

    if not found:
        print("\nContact not found.")


# Function to update a contact
def update_contact():
    print("\n---------- UPDATE CONTACT ----------")

    name = input("Enter name of contact to update: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("\nContact Found!")

            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print("\nContact updated successfully!")
            return

    print("\nContact not found.")


# Function to delete a contact
def delete_contact():
    print("\n---------- DELETE CONTACT ----------")

    name = input("Enter name of contact to delete: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            print("\nContact deleted successfully!")
            return

    print("\nContact not found.")


# Main function
def main():

    while True:

        print("\n================================")
        print("          CONTACT BOOK")
        print("================================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

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
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Start the program
main()
