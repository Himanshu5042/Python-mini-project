
import requests
import streamlit as st

# ------------------------------------------
# COUNTRY INFORMATION FINDER
# Developer: Himanshu Verma
# API: REST Countries
# ------------------------------------------

API_URL = "https://restcountries.com/v3.1"

st.set_page_config(
    page_title="Country Information Finder",
    page_icon="🌍",
    layout="wide"
)


def get_country_info(country_name):
    """Fetch country information using REST Countries API."""

    url = f"{API_URL}/name/{country_name}"

    params = {
        "fullText": "true"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return data[0]


def format_number(value):
    """Format large numbers with commas."""

    if value is None:
        return "N/A"

    return f"{value:,}"


def get_currency_info(currencies):
    """Extract currency names and symbols."""

    if not currencies:
        return "N/A"

    result = []

    for code, details in currencies.items():
        name = details.get("name", "Unknown")
        symbol = details.get("symbol", "")

        result.append(
            f"{name} ({code}) - {symbol}"
        )

    return ", ".join(result)


def get_languages(languages):
    """Extract country languages."""

    if not languages:
        return "N/A"

    return ", ".join(languages.values())


# ------------------------------------------
# APPLICATION INTERFACE
# ------------------------------------------

st.title("🌍 Country Information Finder")

st.markdown(
    "### Explore detailed information about countries worldwide."
)

st.info(
    "Powered by REST Countries API | Free to use"
)

country_name = st.text_input(
    "Enter Country Name",
    placeholder="Example: India, Japan, France, Germany"
)

if st.button("Search Country", type="primary"):

    if not country_name.strip():
        st.warning("Please enter a country name.")

    else:
        try:
            with st.spinner("Fetching country information..."):

                country = get_country_info(
                    country_name.strip()
                )

                if country is None:
                    st.error(
                        "Country not found. Please check the name."
                    )

                    st.session_state.pop("country", None)

                else:
                    st.session_state["country"] = country

        except requests.exceptions.RequestException as error:
            st.error(f"API connection error: {error}")

        except (KeyError, ValueError, TypeError) as error:
            st.error(f"Unable to process country data: {error}")


# ------------------------------------------
# DISPLAY COUNTRY INFORMATION
# ------------------------------------------

if "country" in st.session_state:

    country = st.session_state["country"]

    name = country.get("name", {})
    official_name = name.get("official", "N/A")
    common_name = name.get("common", "N/A")

    st.divider()

    st.header(f"📍 {common_name}")

    # Country flag
    flag = country.get("flags", {}).get("png")

    if flag:
        st.image(
            flag,
            width=200,
            caption=country.get("flags", {}).get(
                "alt", "Country Flag"
            )
        )

    st.write(f"**Official Name:** {official_name}")

    # Main statistics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Population",
            format_number(country.get("population"))
        )

    with col2:
        area = country.get("area")

        st.metric(
            "Area (km²)",
            format_number(
                int(area) if area is not None else None
            )
        )

    with col3:
        st.metric(
            "Independent",
            "Yes" if country.get("independent") else "No"
        )

    st.divider()

    # Country details
    st.subheader("📋 Country Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            "**Capital:**",
            ", ".join(country.get("capital", ["N/A"]))
        )

        st.write(
            "**Region:**",
            country.get("region", "N/A")
        )

        st.write(
            "**Subregion:**",
            country.get("subregion", "N/A")
        )

        st.write(
            "**Continent:**",
            ", ".join(country.get("continents", ["N/A"]))
        )

    with col2:
        st.write(
            "**Country Code:**",
            country.get("cca2", "N/A")
        )

        st.write(
            "**International Code:**",
            country.get("cca3", "N/A")
        )

        st.write(
            "**Driving Side:**",
            country.get("car", {}).get("side", "N/A")
        )

        st.write(
            "**Time Zones:**",
            ", ".join(country.get("timezones", ["N/A"]))
        )

    st.divider()

    # Currency and language
    st.subheader("💰 Currency and Languages")

    st.write(
        "**Currency:**",
        get_currency_info(country.get("currencies"))
    )

    st.write(
        "**Languages:**",
        get_languages(country.get("languages"))
    )

    # Borders
    st.subheader("🗺️ Border Countries")

    borders = country.get("borders", [])

    if borders:
        st.write(", ".join(borders))
    else:
        st.write("No land-bordering countries listed.")

    # Google Maps
    coordinates = country.get("latlng", [])

    if len(coordinates) == 2:
        latitude, longitude = coordinates

        st.subheader("📍 Geographic Location")

        st.map(
            {
                "latitude": [latitude],
                "longitude": [longitude]
            },
            latitude="latitude",
            longitude="longitude",
            zoom=3
        )

        map_url = (
            f"https://www.google.com/maps?q="
            f"{latitude},{longitude}"
        )

        st.link_button(
            "Open Location in Google Maps",
            map_url
        )

    st.caption(
        "Country information is retrieved from REST Countries API."
    )

st.divider()

st.markdown(
    "Developed with ❤️ using Python | Streamlit | REST Countries API"
)
