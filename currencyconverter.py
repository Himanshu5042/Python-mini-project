
# 💱 Currency Converter Using Python

## 📌 Project Overview

Currency Converter is a Python-based application that
allows users to convert one currency into another using
exchange rate information from the Frankfurter API.

The application uses Python and Streamlit to provide
a simple and interactive user interface.

Users can select their source currency, target currency,
enter an amount, and view the converted value.

## ✨ Features

- Convert currencies from around the world.
- Support multiple international currencies.
- Fetch exchange rates using a REST API.
- Display the latest available reference rate.
- Show conversion results instantly.
- Display the exchange rate and its date.
- User-friendly Streamlit dashboard.
- API error handling.
- No API key required.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | API integration |
| Streamlit | Web application interface |
| Frankfurter API | Exchange rate information |
| JSON | API response processing |
| Git & GitHub | Version control |

## 🌐 API Used

### Frankfurter API

Website:
https://frankfurter.dev/

API Documentation:
https://frankfurter.dev/

Currencies endpoint:
https://api.frankfurter.dev/v2/currencies

Exchange rate endpoint example:
https://api.frankfurter.dev/v2/rate/USD/INR

The API does not require an API key.

Note: Frankfurter provides reference exchange rates,
not guaranteed real-time trading or bank transaction rates.
Rates may not update on weekends and public holidays.

## 📂 Project Structure

currency-converter/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Installation Guide

### Step 1: Clone the Repository

git clone https://github.com/himanshu-verma/currency-converter.git

### Step 2: Open the Project Folder

cd currency-converter

### Step 3: Create Virtual Environment

python -m venv venv

### Step 4: Activate Virtual Environment

For Windows:

venv\Scripts\activate

### Step 5: Install Dependencies

pip install -r requirements.txt

### Step 6: Run the Application

streamlit run main.py

The application will open in your browser.

Local URL:

http://localhost:8501

## 🔍 How It Works

1. User opens the Currency Converter application.
2. The application fetches available currencies.
3. User selects the source currency.
4. User selects the target currency.
5. User enters the amount.
6. Python sends a request to the Frankfurter API.
7. The API returns the exchange rate.
8. Python calculates the converted amount.
9. Streamlit displays the result.

## 🧮 Conversion Formula

Converted Amount = Amount × Exchange Rate

Example:

If:

1 USD = 85 INR

Then:

10 USD × 85 = 850 INR

The actual result depends on the API rate available
at the time of conversion.

## 🎯 Learning Outcomes

- Understanding REST APIs.
- Working with HTTP GET requests.
- Processing JSON responses.
- Using Python dictionaries.
- Understanding exchange rates.
- Handling API exceptions.
- Building interactive web applications.
- Using Streamlit.
- Managing Python project dependencies.
- Uploading projects to GitHub.

## ⚠️ Disclaimer

The exchange rates displayed by this application
are reference rates.

They may differ from rates offered by banks,
credit cards, money exchanges, or payment services.

The application is intended for educational purposes.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub:
https://github.com/himanshu-verma

## 📜 License

This project is licensed under the MIT License.

## ⭐ Support

If you find this project useful, please give
the repository a star on GitHub!
