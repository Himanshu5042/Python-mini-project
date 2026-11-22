
# 📚 Google Books Search Engine

A Python-based Google Books Search Engine that allows users to search for books using the Google Books API.

Users can search by book title, author, subject, or keyword and explore book information through a simple Streamlit interface.

## 🚀 Features

- Search books by title.
- Search books by author.
- Search books by subject.
- Search using general keywords.
- Display book cover images.
- Show book title and author details.
- Display publisher and publication date.
- Show page count and language.
- Display book categories and ratings.
- Read book descriptions.
- Open book details on Google Books.
- Choose the number of search results.

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- Google Books API

## 🌐 API Used

Google Books API:

https://www.googleapis.com/books/v1/volumes

Official documentation:

https://developers.google.com/books/docs/v1/using

**API Key:** Not required for this basic project.

## 📁 Project Structure

```text
google-books-search-engine/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/himanshu-verma/google-books-search-engine.git
```

### Step 2: Open the project folder

```bash
cd google-books-search-engine
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

The application will open in your browser.

## 📖 How to Use

1. Open the Google Books Search Engine.
2. Select a search option:
   - All fields
   - Title
   - Author
   - Subject
3. Enter a book name or keyword.
4. Select the number of results.
5. Click the Search Books button.
6. Explore the book information.
7. Click View on Google Books to see more details.

## 🎯 Example Searches

Try searching for:

- Python Programming
- Artificial Intelligence
- Data Science
- Machine Learning
- Computer Networks
- Deep Learning
- Atomic Habits

## 📚 Learning Outcomes

By building this project, you will learn:

- How to work with a REST API.
- How to send HTTP GET requests using Python.
- How to handle JSON responses.
- How to extract data from nested JSON objects.
- How to display API data using Streamlit.
- How to handle API errors and exceptions.
- How to organize and upload a Python project to GitHub.

## 🔮 Future Improvements

- Add advanced book filters.
- Add book recommendations.
- Add pagination for search results.
- Add a personal reading list.
- Add book reviews and ratings.
- Add a database to save favourite books.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub: https://github.com/himanshu-verma

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!
