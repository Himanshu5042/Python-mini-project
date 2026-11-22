
import requests
import streamlit as st

API_URL = "https://www.googleapis.com/books/v1/volumes"

st.set_page_config(
    page_title="Google Books Search Engine",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Google Books Search Engine")
st.write("Search books by title, author, subject, or keyword.")

# Search options
search_type = st.selectbox(
    "Search by",
    ["All fields", "Title", "Author", "Subject"]
)

query = st.text_input(
    "Enter book title, author, or keyword",
    placeholder="Example: Python Programming"
)

max_results = st.slider(
    "Number of results",
    min_value=5,
    max_value=20,
    value=10
)


def search_books(search_query, search_field, limit):
    """Search books using the Google Books API."""

    field_codes = {
        "All fields": "",
        "Title": "intitle:",
        "Author": "inauthor:",
        "Subject": "subject:"
    }

    formatted_query = field_codes[search_field] + search_query

    params = {
        "q": formatted_query,
        "maxResults": limit,
        "printType": "books"
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=15
    )

    response.raise_for_status()
    return response.json()


def display_book(book):
    """Display information about one book."""

    info = book.get("volumeInfo", {})

    title = info.get("title", "Title not available")
    authors = info.get("authors", ["Author not available"])
    publisher = info.get("publisher", "Not available")
    published_date = info.get("publishedDate", "Not available")
    description = info.get("description", "No description available.")
    categories = info.get("categories", ["Not available"])
    page_count = info.get("pageCount", "Not available")
    language = info.get("language", "Not available")
    rating = info.get("averageRating", "Not rated")
    ratings_count = info.get("ratingsCount", 0)

    image_links = info.get("imageLinks", {})
    thumbnail = image_links.get("thumbnail")

    book_link = info.get(
        "infoLink",
        "https://books.google.com/"
    )

    with st.container(border=True):
        col1, col2 = st.columns([1, 3])

        with col1:
            if thumbnail:
                st.image(thumbnail, use_container_width=True)
            else:
                st.write("📖 Cover image unavailable")

        with col2:
            st.subheader(title)
            st.write("**Author(s):**", ", ".join(authors))
            st.write("**Publisher:**", publisher)
            st.write("**Published:**", published_date)
            st.write("**Pages:**", page_count)
            st.write("**Language:**", language)
            st.write("**Category:**", ", ".join(categories))
            st.write(
                f"**Rating:** {rating} / 5 "
                f"({ratings_count} ratings)"
            )

            with st.expander("Read book description"):
                st.write(description, unsafe_allow_html=False)

            st.link_button("View on Google Books", book_link)


# Search button
if st.button("🔍 Search Books", type="primary"):
    if not query.strip():
        st.warning("Please enter a book title, author, or keyword.")

    else:
        try:
            with st.spinner("Searching for books..."):
                data = search_books(query, search_type, max_results)

            books = data.get("items", [])

            if not books:
                st.info("No books found. Try another search keyword.")

            else:
                st.success(
                    f"Found {data.get('totalItems', len(books))} "
                    f"matching books. Showing {len(books)} results."
                )

                for book in books:
                    display_book(book)

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again.")

        except requests.exceptions.RequestException as error:
            st.error(f"API request failed: {error}")

        except (ValueError, KeyError) as error:
            st.error(f"Could not process the book data: {error}")


st.divider()
st.caption("Powered by the Google Books API | Built with Python and Streamlit")
