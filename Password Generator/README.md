# 🔐 Password Generator

A simple **Python Password Generator** that creates strong and random passwords using lowercase letters, uppercase letters, numbers, and special characters.

## 📌 Features

* Generates passwords of user-defined length
* Includes lowercase letters (`a-z`)
* Includes uppercase letters (`A-Z`)
* Includes numbers (`0-9`)
* Includes special characters (`!@#$%^&*`)
* Randomly shuffles the generated password
* Handles invalid user input
* Requires a minimum password length of 4 characters

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* `string` module

## 📂 Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/password-generator.git
```

### 2. Open the project folder

```bash
cd password-generator
```

### 3. Run the Python program

```bash
python password_generator.py
```

## 💻 Example

```text
===== PASSWORD GENERATOR =====
Enter password length: 12

Generated Password: h@7Kp!2Lm#9Q
```

Every time you run the program, a different password can be generated.

## 🔍 How It Works

The program uses Python's `string` module to create different character groups:

```python
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation
```

The program then:

1. Takes the desired password length from the user.
2. Selects at least one lowercase letter.
3. Selects at least one uppercase letter.
4. Selects at least one number.
5. Selects at least one special character.
6. Generates the remaining characters randomly.
7. Shuffles all characters.
8. Displays the final password.

## ⚠️ Important Note

This project is intended as a **Python learning mini-project**.

For passwords intended for real security use, Python's `secrets` module is recommended instead of the `random` module because it is designed for security-sensitive random generation.

## 📚 Concepts Practiced

This project helps practice:

* Functions
* User input
* Conditional statements
* `for` loops
* Lists
* Strings
* Modules
* Exception handling
* Randomization

## 🔮 Future Improvements

Possible upgrades include:

* Add a password strength checker
* Allow users to exclude special characters
* Add a GUI using Tkinter
* Copy the password directly to the clipboard
* Generate multiple passwords at once
* Add a secure `secrets`-based generator
* Save generated passwords securely

## 👨‍💻 Author

**Himanshu Verma**

Python Mini Project — Password Generator
