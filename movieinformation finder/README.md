
# 🎬 Movie Information Finder Using Python

## 📌 Project Overview

Movie Information Finder is a Python-based web application
that allows users to search for movies and explore detailed
information about them.

The application uses the OMDb (Open Movie Database) API
to retrieve movie information and displays the results
through an interactive Streamlit dashboard.

Users can search for movies by title and view movie posters,
release dates, genres, directors, actors, ratings, plot
summaries, awards, and other details.

## ✨ Features

- Search movies by title.
- Display movie posters.
- Show movie release year.
- Display movie genre.
- Show IMDb ratings.
- Display IMDb votes.
- Show Metascore.
- Display movie storyline.
- Show director and writer details.
- Display actors and cast information.
- Show movie awards.
- Display box office information.
- Open movie details on IMDb.
- Handle API errors and invalid searches.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | API integration |
| Streamlit | Dashboard development |
| OMDb API | Movie information |
| JSON | API response processing |
| Python-dotenv | API key management |
| Git & GitHub | Version control |

## 🌐 API Used

### OMDb API (Open Movie Database)

Website:
https://www.omdbapi.com/

API Registration:
https://www.omdbapi.com/apikey.aspx

Documentation:
https://www.omdbapi.com/

Movie Search Endpoint:

https://www.omdbapi.com/?s=Avatar&apikey=YOUR_API_KEY

Movie Details Endpoint:

https://www.omdbapi.com/?i=tt1375666&apikey=YOUR_API_KEY

An API key is required to access movie information.

## 📂 Project Structure

movie-information-finder/
│
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md

## ⚙️ Installation Guide

### Step 1: Clone the Repository

git clone https://github.com/himanshu-verma/movie-information-finder.git

### Step 2: Open Project Folder

cd movie-information-finder

### Step 3: Create Virtual Environment

python -m venv venv

### Step 4: Activate Virtual Environment

For Windows:

venv\Scripts\activate

### Step 5: Install Dependencies

pip install -r requirements.txt

### Step 6: Get OMDb API Key

Visit:

https://www.omdbapi.com/apikey.aspx

Register for an API key.

### Step 7: Configure API Key

Create a file named .env in your project folder.

Add:

OMDB_API_KEY=your_actual_omdb_api_key

Replace the placeholder with your actual API key.

### Step 8: Run the Application

streamlit run main.py

The application will open in your browser.

Local URL:

http://localhost:8501

## 🔍 How It Works

1. User enters a movie name.
2. Python sends a search request to the OMDb API.
3. API returns matching movie information.
4. User selects a movie from the search results.
5. Python sends another request using the IMDb ID.
6. API returns complete movie details.
7. Python processes the JSON response.
8. Streamlit displays the movie information.

## 📊 Information Displayed

| Information | Description |
|---|---|
| Movie Title | Name of the movie |
| Poster | Movie poster image |
| Release Year | Year of release |
| Genre | Movie category |
| Runtime | Movie duration |
| Director | Movie director |
| Writer | Movie writer |
| Actors | Main cast |
| IMDb Rating | IMDb rating |
| IMDb Votes | Number of IMDb votes |
| Metascore | Metacritic score |
| Plot | Movie storyline |
| Awards | Movie awards |
| Box Office | Box office information |

## 🎯 Learning Outcomes

- Understanding REST APIs.
- Making HTTP GET requests.
- Processing JSON responses.
- Working with Python dictionaries.
- Understanding API parameters.
- Handling API exceptions.
- Using environment variables.
- Managing API keys securely.
- Developing Streamlit applications.
- Integrating external APIs.
- Managing GitHub repositories.

## 🔐 Security

Never upload your actual API key to GitHub.

The .env file is included in .gitignore
to prevent accidental API key exposure.

Use .env.example as a configuration template.

## ⚠️ Disclaimer

This application is developed for educational purposes.

Movie information, posters, and ratings are provided
by the OMDb API.

API request limits and available information depend
on the selected API subscription plan.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub:
https://github.com/himanshu-verma

## 📜 License

This project is licensed under the MIT License.

## ⭐ Support

If you like this project, please give the repository
a star on GitHub!
