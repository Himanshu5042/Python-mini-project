# 🔄 Unit Converter

A simple **Python Unit Converter** that allows users to convert different units of **length, weight, temperature, and time** through a menu-driven command-line interface.

## 📌 Features

* Convert kilometers to miles
* Convert miles to kilometers
* Convert meters to feet
* Convert feet to meters
* Convert kilograms to pounds
* Convert pounds to kilograms
* Convert grams to kilograms
* Convert kilograms to grams
* Convert Celsius to Fahrenheit
* Convert Fahrenheit to Celsius
* Convert Celsius to Kelvin
* Convert Kelvin to Celsius
* Convert hours to minutes
* Convert minutes to hours
* Convert minutes to seconds
* Convert seconds to minutes
* Handles invalid input

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Conditional Statements
* Loops
* Exception Handling
* Mathematical Operations

## 📂 Project Structure

```text
unit-converter/
│
├── unit_converter.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/unit-converter.git
```

### 2. Open the project folder

```bash
cd unit-converter
```

### 3. Run the program

```bash
python unit_converter.py
```

## 💻 Example

```text
==============================
       UNIT CONVERTER
==============================
1. Length
2. Weight
3. Temperature
4. Time
5. Exit

Enter your choice: 1

--- Length Converter ---
1. Kilometers to Miles
2. Miles to Kilometers
3. Meters to Feet
4. Feet to Meters

Enter your choice: 1
Enter value: 10

10 km = 6.21 miles
```

## 🌡️ Temperature Example

```text
--- Temperature Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius

Enter your choice: 1
Enter temperature: 25

25°C = 77.00°F
```

## ⚖️ Weight Example

```text
--- Weight Converter ---
1. Kilograms to Pounds
2. Pounds to Kilograms
3. Grams to Kilograms
4. Kilograms to Grams

Enter your choice: 1
Enter value: 5

5 kg = 11.02 pounds
```

## ⏱️ Time Example

```text
--- Time Converter ---
1. Hours to Minutes
2. Minutes to Hours
3. Minutes to Seconds
4. Seconds to Minutes

Enter your choice: 1
Enter value: 2

2 hours = 120.00 minutes
```

## 🔍 How It Works

The program uses separate functions for each type of conversion.

### Length

Conversion formulas include:

```text
1 km = 0.621371 miles
1 mile = 1.60934 km
1 meter = 3.28084 feet
1 foot = 0.3048 meters
```

### Weight

```text
1 kg = 2.20462 pounds
1 pound = 0.453592 kg
1 kg = 1000 grams
1 gram = 0.001 kg
```

### Temperature

```text
Fahrenheit = (Celsius × 9/5) + 32

Celsius = (Fahrenheit - 32) × 5/9

Kelvin = Celsius + 273.15
```

### Time

```text
1 hour = 60 minutes
1 minute = 60 seconds
```

## 📚 Python Concepts Practiced

This project helps practice:

* Variables
* User input
* Functions
* `while` loops
* `if-elif-else`
* Mathematical operations
* Exception handling
* Formatted output
* Menu-driven programming

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add area conversion
* [ ] Add volume conversion
* [ ] Add speed conversion
* [ ] Add data storage units
* [ ] Add currency conversion using an API
* [ ] Add a graphical interface using Tkinter
* [ ] Add more international units
* [ ] Add conversion history
* [ ] Add a web interface using Flask

## 🎯 Project Objective

The objective of this project is to build a simple and practical Python application while learning **functions, mathematical calculations, conditional statements, loops, and exception handling**.

## 👨‍💻 Author

**Himanshu Verma**

Python Mini Project — Unit Converter
