
# 😂 Random Joke Generator Using Python

A fun and interactive Random Joke Generator developed using Python and Streamlit.

This application uses the Official Joke API to fetch random jokes. Users can select joke categories, view jokes, and save their favourite jokes during the current session.

## 🚀 Features

- Generate random jokes instantly.
- Select different joke categories.
- General jokes.
- Programming jokes.
- Knock-knock jokes.
- Display joke setup and punchline.
- Save favourite jokes.
- View saved jokes during the session.
- Simple and interactive user interface.
- Handle API errors and connection timeouts.

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- Official Joke API

## 🌐 API Used

**Official Joke API**

API URL:

https://official-joke-api.appspot.com

Documentation and examples:

https://official-joke-api.appspot.com/

No API key is required.

## 📁 Project Structure

```text
random-joke-generator/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/himanshu-verma/random-joke-generator.git
```

### Step 2: Open the project folder

```bash
cd random-joke-generator
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
streamlit run main.py
```

The application will open in your web browser.

## 📖 How to Use

1. Open the Random Joke Generator.
2. Select a joke category.
3. Click the Generate Random Joke button.
4. Read the joke setup and punchline.
5. Click Save to Favourites to save a joke.
6. Open the Favourite Jokes section to view saved jokes.
7. Generate another joke whenever you want.

## 🎯 Available Joke Categories

| Category | Description |
|---|---|
| Any | Random joke |
| General | General entertainment jokes |
| Programming | Computer and coding jokes |
| Knock-knock | Knock-knock jokes |

## 🧠 Learning Outcomes

By completing this project, you will learn:

- How to use REST APIs in Python.
- How to send HTTP GET requests.
- How to process JSON responses.
- How to use Python functions.
- How to handle API errors.
- How to use Streamlit session state.
- How to create interactive web applications.
- How to organize Python projects for GitHub.

## 🔮 Future Improvements

- Add a joke search feature.
- Add a daily joke notification.
- Add a copy joke button.
- Export favourite jokes to a text file.
- Store favourite jokes in SQLite.
- Add more joke categories.
- Add a dark mode interface.

## ⚠️ Important Note

The application requires an internet connection to fetch jokes from the API.

Favourite jokes are stored in Streamlit session state and are not permanently saved. They may be lost when the session resets.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub: https://github.com/himanshu-verma

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!
