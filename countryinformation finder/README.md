
# 🌍 Country Information Finder Using Python

## 📌 Project Overview

Country Information Finder is a Python-based web application
that allows users to explore detailed information about
countries around the world.

The application uses the REST Countries API to retrieve
country information and displays it through an interactive
Streamlit dashboard.

Users can search for a country and view its flag, capital,
population, area, currency, languages, time zones,
geographical location, and neighboring countries.

## ✨ Features

- Search countries by name.
- Display country flags.
- Show official and common country names.
- Display capital cities.
- Show population statistics.
- Display geographical area.
- Show region and subregion.
- Display country currencies and symbols.
- Show official languages.
- Display country codes.
- Show neighboring countries.
- Display time zones.
- Show geographical location on a map.
- Open country location in Google Maps.
- Handle API errors and invalid country names.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | API integration |
| Streamlit | Dashboard development |
| REST Countries API | Country information |
| JSON | API response processing |
| Git & GitHub | Version control |

## 🌐 API Used

### REST Countries API

Website:
https://restcountries.com/

API Documentation:
https://restcountries.com/

Country search endpoint:

https://restcountries.com/v3.1/name/india?fullText=true

This API provides country details without requiring
an API key.

## 📂 Project Structure

country-information-finder/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Installation Guide

### Step 1: Clone the Repository

git clone https://github.com/himanshu-verma/country-information-finder.git

### Step 2: Open Project Folder

cd country-information-finder

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

1. User enters a country name.
2. Python sends an HTTP GET request.
3. REST Countries API processes the request.
4. API returns country information in JSON format.
5. Python extracts the required information.
6. Streamlit displays the country details.
7. User can explore the geographical location.

## 📊 Information Displayed

| Information | Description |
|---|---|
| Country Name | Common country name |
| Official Name | Official country name |
| Flag | National flag |
| Capital | Capital city |
| Population | Total population |
| Area | Area in square kilometres |
| Region | Geographical region |
| Currency | Official currency |
| Languages | Spoken/official languages |
| Time Zones | Country time zones |
| Borders | Neighboring countries |
| Coordinates | Latitude and longitude |

## 🎯 Learning Outcomes

- Understanding REST APIs.
- Making HTTP GET requests.
- Processing JSON data.
- Working with Python dictionaries.
- Handling API errors.
- Using Streamlit for web development.
- Displaying maps in Python.
- Integrating external APIs.
- Managing GitHub repositories.

## ⚠️ Disclaimer

Country information is retrieved from the REST Countries API.
Some fields may be unavailable or incomplete depending
on the API response.

The displayed population and other country statistics
may not represent the latest official figures.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub:
https://github.com/himanshu-verma

## 📜 License

This project is licensed under the MIT License.

## ⭐ Support

If you like this project, please give the repository
a star on GitHub!
