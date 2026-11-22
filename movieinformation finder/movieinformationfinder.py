
import os
import requests
import streamlit as st
from dotenv import load_dotenv

# -----------------------------------------
# MOVIE INFORMATION FINDER
# Developer: Himanshu Verma
# API: OMDb (Open Movie Database)
# -----------------------------------------

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "https://www.omdbapi.com/"

st.set_page_config(
    page_title="Movie Information Finder",
    page_icon="🎬",
    layout="wide"
)


# -----------------------------------------
# SEARCH MOVIES
# -----------------------------------------

@st.cache_data(ttl=3600)
def search_movies(title):
    """Search movies using their title."""

    params = {
        "apikey": API_KEY,
        "s": title,
        "type": "movie"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=15
    )

    response.raise_for_status()
    data = response.json()

    if data.get("Response") == "True":
        return data.get("Search", [])

    return []


# -----------------------------------------
# GET MOVIE DETAILS
# -----------------------------------------

@st.cache_data(ttl=3600)
def get_movie_details(imdb_id):
    """Fetch complete movie information."""

    params = {
        "apikey": API_KEY,
        "i": imdb_id,
        "plot": "full"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=15
    )

    response.raise_for_status()
    data = response.json()

    if data.get("Response") == "True":
        return data

    return None


# -----------------------------------------
# DISPLAY MOVIE DETAILS
# -----------------------------------------

def display_movie(movie):
    """Display complete movie information."""

    st.divider()

    st.header(f"🎬 {movie.get('Title', 'Unknown')}")

    col1, col2 = st.columns([1, 2])

    with col1:
        poster = movie.get("Poster")

        if poster and poster != "N/A":
            st.image(
                poster,
                caption=movie.get("Title"),
                use_container_width=True
            )
        else:
            st.info("Movie poster is not available.")

    with col2:
        st.subheader("Movie Overview")

        st.write(
            f"**Release Year:** {movie.get('Year', 'N/A')}"
        )

        st.write(
            f"**Rated:** {movie.get('Rated', 'N/A')}"
        )

        st.write(
            f"**Released:** {movie.get('Released', 'N/A')}"
        )

        st.write(
            f"**Runtime:** {movie.get('Runtime', 'N/A')}"
        )

        st.write(
            f"**Genre:** {movie.get('Genre', 'N/A')}"
        )

        st.write(
            f"**Language:** {movie.get('Language', 'N/A')}"
        )

        st.write(
            f"**Country:** {movie.get('Country', 'N/A')}"
        )

    st.subheader("⭐ Ratings")

    ratings = movie.get("Ratings", [])

    imdb_rating = movie.get("imdbRating", "N/A")
    imdb_votes = movie.get("imdbVotes", "N/A")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("IMDb Rating", imdb_rating)

    with c2:
        st.metric("IMDb Votes", imdb_votes)

    with c3:
        st.metric("Metascore", movie.get("Metascore", "N/A"))

    if ratings:
        st.write("**Other Ratings:**")

        for rating in ratings:
            st.write(
                f"- {rating.get('Source', 'Unknown')}: "
                f"{rating.get('Value', 'N/A')}"
            )

    st.divider()

    st.subheader("📖 Storyline")

    st.write(movie.get("Plot", "Plot not available."))

    st.subheader("🎭 Cast and Crew")

    c1, c2 = st.columns(2)

    with c1:
        st.write(
            f"**Director:** {movie.get('Director', 'N/A')}"
        )

        st.write(
            f"**Writer:** {movie.get('Writer', 'N/A')}"
        )

    with c2:
        st.write(
            f"**Actors:** {movie.get('Actors', 'N/A')}"
        )

        st.write(
            f"**Awards:** {movie.get('Awards', 'N/A')}"
        )

    st.write(
        f"**Production:** {movie.get('Production', 'N/A')}"
    )

    st.write(
        f"**Box Office:** {movie.get('BoxOffice', 'N/A')}"
    )

    imdb_id = movie.get("imdbID")

    if imdb_id:
        st.link_button(
            "View on IMDb",
            f"https://www.imdb.com/title/{imdb_id}/"
        )


# -----------------------------------------
# APPLICATION INTERFACE
# -----------------------------------------

st.title("🎬 Movie Information Finder")

st.markdown(
    "### Discover movies and explore their complete details."
)

st.info(
    "Powered by OMDb API | Python | Streamlit"
)

if not API_KEY:
    st.error(
        "OMDb API key not found. Please configure your .env file."
    )
    st.stop()


# Search input
movie_name = st.text_input(
    "Enter Movie Name",
    placeholder="Example: Interstellar, Inception, Avatar"
)

if st.button("Search Movie", type="primary"):

    if not movie_name.strip():
        st.warning("Please enter a movie name.")

    else:
        try:
            with st.spinner("Searching for movies..."):

                results = search_movies(movie_name.strip())

                st.session_state["movie_results"] = results
                st.session_state.pop("selected_movie", None)

                if not results:
                    st.warning(
                        "No movies found. Try another movie title."
                    )

        except requests.exceptions.RequestException as error:
            st.error(f"API connection error: {error}")


# -----------------------------------------
# DISPLAY SEARCH RESULTS
# -----------------------------------------

if "movie_results" in st.session_state:

    results = st.session_state["movie_results"]

    if results:

        st.subheader("🔎 Search Results")

        options = {
            (
                f"{movie.get('Title', 'Unknown')} "
                f"({movie.get('Year', 'N/A')})"
            ): movie["imdbID"]
            for movie in results
        }

        selected_title = st.selectbox(
            "Select a movie to view details",
            list(options.keys())
        )

        if st.button("View Movie Details"):

            try:
                with st.spinner("Loading movie information..."):

                    movie = get_movie_details(
                        options[selected_title]
                    )

                    if movie:
                        st.session_state["selected_movie"] = movie
                    else:
                        st.error("Movie details are unavailable.")

            except requests.exceptions.RequestException as error:
                st.error(f"API connection error: {error}")


# -----------------------------------------
# SHOW SELECTED MOVIE
# -----------------------------------------

if "selected_movie" in st.session_state:

    display_movie(st.session_state["selected_movie"])


# -----------------------------------------
# FOOTER
# -----------------------------------------

st.divider()

st.markdown(
    "Developed with ❤️ by Himanshu Verma"
)

st.caption(
    "Movie data provided by OMDb API. "
    "Ratings and information may vary."
)
