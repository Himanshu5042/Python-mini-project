
import requests
import streamlit as st
from io import BytesIO

API_URL = "https://dog.ceo/api"

st.set_page_config(
    page_title="Random Dog Image Generator",
    page_icon="🐶",
    layout="centered"
)

st.title("🐶 Random Dog Image Generator")
st.write("Discover adorable dogs with just one click!")

# Store the current dog image in session
if "dog_image" not in st.session_state:
    st.session_state.dog_image = None


def get_breeds():
    """Fetch all available dog breeds."""

    response = requests.get(
        f"{API_URL}/breeds/list/all",
        timeout=15
    )
    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError("Could not retrieve dog breeds.")

    return data.get("message", {})


def get_random_dog(breed=None):
    """Fetch a random dog image."""

    if breed and breed != "All Breeds":
        breed_parts = breed.split()

        if len(breed_parts) == 1:
            endpoint = f"{API_URL}/breed/{breed_parts[0]}/images/random"
        else:
            main_breed = breed_parts[0]
            sub_breed = breed_parts[1]
            endpoint = (
                f"{API_URL}/breed/{main_breed}/"
                f"{sub_breed}/images/random"
            )
    else:
        endpoint = f"{API_URL}/breeds/image/random"

    response = requests.get(endpoint, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError("Could not retrieve a dog image.")

    return data["message"]


# Load breeds
try:
    breeds_data = get_breeds()

    breed_options = ["All Breeds"]

    for breed, sub_breeds in breeds_data.items():
        if sub_breeds:
            for sub_breed in sub_breeds:
                breed_options.append(f"{breed} {sub_breed}")
        else:
            breed_options.append(breed)

except requests.exceptions.RequestException:
    breeds_data = {}
    breed_options = ["All Breeds"]
    st.warning("Could not load breeds. You can still try random dogs.")

# Breed selection
selected_breed = st.selectbox(
    "Choose a dog breed",
    breed_options
)

# Generate image
if st.button("🐕 Generate Random Dog", type="primary"):
    try:
        with st.spinner("Finding a cute dog..."):
            st.session_state.dog_image = get_random_dog(
                selected_breed
            )

    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")

    except requests.exceptions.RequestException as error:
        st.error(f"API error: {error}")

    except (ValueError, KeyError) as error:
        st.error(f"Unable to get dog image: {error}")

# Display dog image
if st.session_state.dog_image:
    image_url = st.session_state.dog_image

    st.success("Here is your adorable dog!")

    try:
        image_response = requests.get(
            image_url,
            timeout=20
        )
        image_response.raise_for_status()

        image_bytes = image_response.content

        st.image(
            image_bytes,
            caption="Your Random Dog 🐶",
            use_container_width=True
        )

        st.download_button(
            label="⬇️ Download Dog Image",
            data=image_bytes,
            file_name="random_dog.jpg",
            mime=image_response.headers.get(
                "Content-Type",
                "image/jpeg"
            )
        )

    except requests.exceptions.RequestException as error:
        st.error(f"Could not load the image: {error}")

st.divider()
st.caption("Powered by Dog CEO API | Built with Python and Streamlit")
