# 📞 Contact Book

A simple **Python Contact Book** that allows users to manage their contacts from the command line.

Users can **add, view, search, update, and delete contacts** using a simple menu-driven interface.

## 📌 Features

* Add new contacts
* View all contacts
* Search contacts by name
* Update contact information
* Delete contacts
* Simple command-line interface
* Easy-to-understand Python code

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* String Methods

## 📂 Project Structure

```text
contact-book/
│
├── contact_book.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/contact-book.git
```

### 2. Open the project folder

```bash
cd contact-book
```

### 3. Run the Python program

```bash
python contact_book.py
```

## 💻 Example

```text
==============================
        CONTACT BOOK
==============================
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1

--- Add Contact ---
Enter name: Rahul
Enter phone number: 9876543210
Enter email: rahul@gmail.com
Enter address: Delhi

Contact added successfully!
```

## 📋 View Contacts

After adding contacts, select option `2`:

```text
--- All Contacts ---

Contact 1
Name: Rahul
Phone: 9876543210
Email: rahul@gmail.com
Address: Delhi

Contact 2
Name: Aman
Phone: 9876501234
Email: aman@gmail.com
Address: Noida
```

## 🔎 Search Contact

Select option `3` and enter the name:

```text
--- Search Contact ---

Enter name to search: Rahul

Contact Found!
Name: Rahul
Phone: 9876543210
Email: rahul@gmail.com
Address: Delhi
```

## ✏️ Update Contact

Select option `4`:

```text
--- Update Contact ---

Enter the name of the contact to update: Rahul

Contact found.
Enter new phone number: 9999999999
Enter new email: rahul_new@gmail.com
Enter new address: Gurugram

Contact updated successfully!
```

## 🗑️ Delete Contact

Select option `5`:

```text
--- Delete Contact ---

Enter the name of the contact to delete: Rahul

Contact deleted successfully!
```

## 🔍 How It Works

Each contact is stored as a Python dictionary:

```python
contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "address": address
}
```

All contacts are stored inside a list:

```python
contacts = []
```

The program uses different functions to perform operations on this list.

### Add

Adds a new dictionary to the `contacts` list.

### View

Loops through the list and displays all contacts.

### Search

Uses the contact name to find a matching contact.

### Update

Finds an existing contact and replaces its phone, email, and address.

### Delete

Removes the selected contact from the list.

## 📚 Python Concepts Practiced

This project helps practice:

* Variables
* User input
* Lists
* Dictionaries
* Functions
* `for` loops
* `while` loops
* `if-elif-else`
* String methods
* CRUD operations

## 🔮 Future Improvements

Possible improvements include:

* [ ] Save contacts to a CSV file
* [ ] Save contacts using JSON
* [ ] SQLite database support
* [ ] Search by phone number
* [ ] Search by email
* [ ] Sort contacts alphabetically
* [ ] Import and export contacts
* [ ] Add a graphical user interface using Tkinter
* [ ] Add contact groups
* [ ] Add duplicate-contact detection

## 🎯 Project Objective

The objective of this project is to create a simple contact management system while learning the fundamentals of Python programming and CRUD operations.

## 👨‍💻 Author

**Himanshu Verma**

Python Mini Project — Contact Book
