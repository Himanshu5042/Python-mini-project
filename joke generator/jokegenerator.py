
import requests
import streamlit as st

API_URL = "https://official-joke-api.appspot.com"

st.set_page_config(
    page_title="Random Joke Generator",
    page_icon="😂",
    layout="centered"
)

st.title("😂 Random Joke Generator")
st.write("Need a laugh? Generate a random joke using Python!")

# Store favourite jokes in session state
if "favourites" not in st.session_state:
    st.session_state.favourites = []

if "current_joke" not in st.session_state:
    st.session_state.current_joke = None


def get_random_joke(category):
    """Fetch a random joke from the Official Joke API."""

    if category == "Any":
        endpoint = f"{API_URL}/random_joke"
    else:
        endpoint = f"{API_URL}/jokes/{category}/random"

    response = requests.get(endpoint, timeout=15)
    response.raise_for_status()

    data = response.json()

    # Category endpoints return a list
    if isinstance(data, list):
        if not data:
            return None
        return data[0]

    return data


# Joke category selection
category = st.selectbox(
    "Choose a joke category",
    [
        "Any",
        "general",
        "programming",
        "knock-knock"
    ]
)

# Generate joke
if st.button("🎲 Generate Random Joke", type="primary"):
    try:
        with st.spinner("Finding a funny joke..."):
            joke = get_random_joke(category)

        if joke:
            st.session_state.current_joke = joke
        else:
            st.warning("No joke found. Please try again.")

    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")

    except requests.exceptions.RequestException as error:
        st.error(f"Unable to fetch joke: {error}")

# Display current joke
joke = st.session_state.current_joke

if joke:
    st.divider()

    st.subheader("🤣 Your Random Joke")

    st.markdown(f"**Setup:** {joke.get('setup', 'Not available')}")

    st.markdown(
        f"**Punchline:** {joke.get('punchline', 'Not available')}"
    )

    st.caption(
        f"Category: {joke.get('type', 'Unknown')} | "
        f"Joke ID: {joke.get('id', 'N/A')}"
    )

    joke_text = (
        f"Setup: {joke.get('setup', '')}\n"
        f"Punchline: {joke.get('punchline', '')}"
    )

    if st.button("❤️ Save to Favourites"):
        if joke_text not in st.session_state.favourites:
            st.session_state.favourites.append(joke_text)
            st.success("Joke saved to favourites!")
        else:
            st.info("This joke is already in your favourites.")

# Favourite jokes
st.divider()
st.subheader("❤️ Favourite Jokes")

if st.session_state.favourites:
    for index, favourite in enumerate(
        st.session_state.favourites,
        start=1
    ):
        with st.expander(f"Favourite Joke {index}"):
            st.write(favourite)
else:
    st.info("You haven't saved any favourite jokes yet.")

st.caption("Powered by Official Joke API | Built with Python and Streamlit")
